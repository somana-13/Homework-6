"""
Tests for the calculator application implementation
"""
import pytest
from unittest.mock import patch, MagicMock
from calculator_app import CalculatorApp

class TestCalculatorApp:
    """Test class for calculator application"""
    
    def test_init(self):
        """Test initialization of calculator application"""
        app = CalculatorApp()
        assert isinstance(app.commands, dict)
        assert app.running is True
        
        # Check if core commands are registered
        assert 'add' in app.commands
        assert 'subtract' in app.commands
        assert 'multiply' in app.commands
        assert 'divide' in app.commands
        assert 'exit' in app.commands
        assert 'menu' in app.commands
    
    def test_parse_input(self):
        """Test parsing of user input"""
        app = CalculatorApp()
        
        # Test basic command parsing
        cmd, args = app.parse_input("add 2 3")
        assert cmd == "add"
        assert args == ["2", "3"]
        
        # Test empty input
        cmd, args = app.parse_input("")
        assert cmd == ""
        assert args == []
        
        # Test command with quoted arguments
        cmd, args = app.parse_input('add "1.5" "2.5"')
        assert cmd == "add"
        assert args == ["1.5", "2.5"]
        
        # Test command with mixed arguments
        cmd, args = app.parse_input('divide 10 "2.5"')
        assert cmd == "divide"
        assert args == ["10", "2.5"]
    
    def test_execute_command_valid(self):
        """Test execution of valid commands"""
        app = CalculatorApp()
        
        # Test add command
        result = app.execute_command("add", ["2", "3"])
        assert result == "5.0"
        
        # Test subtract command
        result = app.execute_command("subtract", ["5", "3"])
        assert result == "2.0"
        
        # Test multiply command
        result = app.execute_command("multiply", ["2", "3"])
        assert result == "6.0"
        
        # Test divide command
        result = app.execute_command("divide", ["6", "3"])
        assert result == "2.0"
        
        # Test menu command
        result = app.execute_command("menu", [])
        assert "Available Commands" in result
        assert "add" in result
        assert "subtract" in result
    
    def test_execute_command_invalid(self):
        """Test execution of invalid commands"""
        app = CalculatorApp()
        
        # Test unknown command
        result = app.execute_command("unknown", [])
        assert "Unknown command" in result
        
        # Test add command with invalid arguments
        result = app.execute_command("add", ["one", "two"])
        assert "Error" in result
        
        # Test divide by zero
        result = app.execute_command("divide", ["5", "0"])
        assert "Error" in result
        assert "divide by zero" in result.lower()
    
    def test_exit_command(self):
        """Test exit command functionality"""
        app = CalculatorApp()
        
        # Test exit command
        result = app.execute_command("exit", [])
        assert "Exiting" in result
        assert app.running is False
        
        # Reset for next test
        app.running = True
        
        # Test quit command (alias for exit)
        result = app.execute_command("quit", [])
        assert "Exiting" in result
        assert app.running is False
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_run(self, mock_print, mock_input):
        """Test the REPL run loop"""
        # Setup mock to exit after one command
        mock_input.side_effect = ["add 2 3", KeyboardInterrupt()]
        
        app = CalculatorApp()
        app.run()
        
        # Verify the app tried to process the command
        assert mock_print.call_count > 2  # Welcome message + menu + result
