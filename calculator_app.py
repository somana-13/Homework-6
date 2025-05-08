"""
Calculator Application with REPL interface and command pattern
"""
import sys
import shlex
from typing import Dict, List, Optional

from commands.command_interface import Command
from commands.calculator_commands import (
    AddCommand, SubtractCommand, MultiplyCommand, 
    DivideCommand, MenuCommand, ExitCommand
)
from plugins.plugin_manager import PluginManager
from calculator.calculations import Calculations

class CalculatorApp:
    """
    Calculator Application implementing a REPL interface with the command pattern
    and plugin architecture for extensibility
    """
    
    def __init__(self):
        """Initialize the calculator application with commands and plugins"""
        self.commands: Dict[str, Command] = {}
        self.running = True
        
        # Register core commands
        self._register_core_commands()
        
        # Load plugin commands
        self._load_plugin_commands()
        
        # Register menu command (needs access to commands dictionary)
        self.commands['menu'] = MenuCommand(self.commands)
        
    def _register_core_commands(self) -> None:
        """Register core calculator commands"""
        self.commands['add'] = AddCommand()
        self.commands['subtract'] = SubtractCommand()
        self.commands['multiply'] = MultiplyCommand()
        self.commands['divide'] = DivideCommand()
        self.commands['exit'] = ExitCommand()
        self.commands['quit'] = ExitCommand()
        
    def _load_plugin_commands(self) -> None:
        """Load and register plugin commands"""
        plugin_manager = PluginManager()
        plugin_commands = plugin_manager.load_plugins()
        
        # Add all discovered plugin commands to the command registry
        self.commands.update(plugin_commands)
    
    def execute_command(self, command_name: str, args: List[str]) -> Optional[str]:
        """
        Execute the specified command with given arguments
        Returns command result or None if command not found
        """
        command = self.commands.get(command_name.lower())
        
        if command is None:
            return f"Unknown command: {command_name}. Type 'menu' to see available commands."
        
        try:
            result = command.execute(*args)
            
            # If it's a calculation command, store in history
            if command_name.lower() in ['add', 'subtract', 'multiply', 'divide']:
                # Convert string args to float
                float_args = [float(arg) for arg in args]
                if len(float_args) >= 2:
                    from calculator.calculator import Calculator
                    from calculator.calculation import Calculation
                    
                    # Create and store calculation in history
                    calculation = Calculator.create_calculation(
                        float_args[0], float_args[1], command_name.lower()
                    )
                    Calculations.add_calculation(calculation)
            
            # Check for exit command
            if isinstance(result, bool) and not result:
                self.running = False
                return "Exiting calculator application. Goodbye!"
                
            return str(result)
            
        except ValueError as e:
            return f"Error: {e}"
        except ZeroDivisionError as e:
            return f"Error: {e}"
        except Exception as e:
            return f"Unexpected error: {e}"
    
    def parse_input(self, user_input: str) -> tuple:
        """
        Parse user input into command name and arguments
        Returns tuple of (command_name, args)
        """
        # Use shlex to handle quoted arguments correctly
        parts = shlex.split(user_input)
        
        if not parts:
            return ('', [])
            
        command_name = parts[0].lower()
        args = parts[1:]
        
        return (command_name, args)
    
    def run(self) -> None:
        """Run the calculator REPL loop"""
        print("Welcome to the Calculator Application!")
        print("Type 'menu' to see available commands or 'exit' to quit.")
        print("=" * 50)
        
        # Show menu at startup
        print(self.execute_command('menu', []))
        
        # Main REPL loop
        while self.running:
            try:
                # Read
                user_input = input("calculator> ")
                
                # Parse
                command_name, args = self.parse_input(user_input)
                
                if not command_name:
                    continue
                
                # Evaluate and Print
                result = self.execute_command(command_name, args)
                print(result)
                
            except KeyboardInterrupt:
                print("\nExiting calculator application. Goodbye!")
                self.running = False
            except EOFError:
                print("\nExiting calculator application. Goodbye!")
                self.running = False
            except Exception as e:
                print(f"Error: {e}")

def main():
    """Main entry point for the calculator application"""
    app = CalculatorApp()
    app.run()

if __name__ == "__main__":
    main()
