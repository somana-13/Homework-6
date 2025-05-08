"""
Tests for the calculator commands implementation
"""
import pytest
from commands.calculator_commands import (
    AddCommand, SubtractCommand, MultiplyCommand, 
    DivideCommand, MenuCommand, ExitCommand
)
from commands.command_interface import Command

class TestCalculatorCommands:
    """Test class for calculator commands"""

    def test_add_command(self):
        """Test add command functionality"""
        # Instantiate command
        command = AddCommand()
        
        # Test execution
        assert command.execute("2", "3") == 5.0
        assert command.execute("2", "3", "4") == 9.0
        assert command.execute("-1", "1") == 0.0
        
        # Test description and usage
        assert isinstance(command.description, str)
        assert len(command.description) > 0
        assert isinstance(command.usage, str)
        assert len(command.usage) > 0
        
        # Test error cases
        with pytest.raises(ValueError):
            command.execute()
        with pytest.raises(ValueError):
            command.execute("1")
        with pytest.raises(ValueError):
            command.execute("one", "two")
    
    def test_subtract_command(self):
        """Test subtract command functionality"""
        # Instantiate command
        command = SubtractCommand()
        
        # Test execution
        assert command.execute("5", "3") == 2.0
        assert command.execute("10", "2", "3") == 5.0
        assert command.execute("0", "1") == -1.0
        
        # Test description and usage
        assert isinstance(command.description, str)
        assert len(command.description) > 0
        assert isinstance(command.usage, str)
        assert len(command.usage) > 0
        
        # Test error cases
        with pytest.raises(ValueError):
            command.execute()
        with pytest.raises(ValueError):
            command.execute("1")
        with pytest.raises(ValueError):
            command.execute("one", "two")
    
    def test_multiply_command(self):
        """Test multiply command functionality"""
        # Instantiate command
        command = MultiplyCommand()
        
        # Test execution
        assert command.execute("2", "3") == 6.0
        assert command.execute("2", "3", "4") == 24.0
        assert command.execute("-1", "5") == -5.0
        
        # Test description and usage
        assert isinstance(command.description, str)
        assert len(command.description) > 0
        assert isinstance(command.usage, str)
        assert len(command.usage) > 0
        
        # Test error cases
        with pytest.raises(ValueError):
            command.execute()
        with pytest.raises(ValueError):
            command.execute("1")
        with pytest.raises(ValueError):
            command.execute("one", "two")
    
    def test_divide_command(self):
        """Test divide command functionality"""
        # Instantiate command
        command = DivideCommand()
        
        # Test execution
        assert command.execute("6", "3") == 2.0
        assert command.execute("24", "2", "3") == 4.0
        assert command.execute("-10", "2") == -5.0
        
        # Test description and usage
        assert isinstance(command.description, str)
        assert len(command.description) > 0
        assert isinstance(command.usage, str)
        assert len(command.usage) > 0
        
        # Test error cases
        with pytest.raises(ValueError):
            command.execute()
        with pytest.raises(ValueError):
            command.execute("1")
        with pytest.raises(ValueError):
            command.execute("one", "two")
        with pytest.raises(ZeroDivisionError):
            command.execute("5", "0")
    
    def test_menu_command(self):
        """Test menu command functionality"""
        # Create mock commands dictionary
        commands = {
            'test1': AddCommand(),
            'test2': SubtractCommand()
        }
        
        # Instantiate command
        command = MenuCommand(commands)
        
        # Test execution
        result = command.execute()
        assert isinstance(result, str)
        assert "Available Commands" in result
        assert "test1" in result
        assert "test2" in result
        
        # Test description and usage
        assert isinstance(command.description, str)
        assert len(command.description) > 0
        assert isinstance(command.usage, str)
        assert len(command.usage) > 0
    
    def test_exit_command(self):
        """Test exit command functionality"""
        # Instantiate command
        command = ExitCommand()
        
        # Test execution
        assert command.execute() is False
        
        # Test description and usage
        assert isinstance(command.description, str)
        assert len(command.description) > 0
        assert isinstance(command.usage, str)
        assert len(command.usage) > 0
