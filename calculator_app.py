"""
Calculator Application with REPL interface and command pattern
Enhanced with logging and environment variables
"""
import sys
import shlex
import os
from typing import Dict, List, Optional

from commands.command_interface import Command
from commands.calculator_commands import (
    AddCommand, SubtractCommand, MultiplyCommand, 
    DivideCommand, MenuCommand, ExitCommand
)
from plugins.plugin_manager import PluginManager
from calculator.calculations import Calculations
from utils.logger import get_logger
from utils.env_config import EnvConfig

class CalculatorApp:
    """
    Calculator Application implementing a REPL interface with the command pattern
    and plugin architecture for extensibility.
    Enhanced with logging and environment variable support.
    """
    
    def __init__(self):
        """Initialize the calculator application with commands and plugins"""
        # Set up logger
        self.logger = get_logger(__name__)
        self.logger.info("Initializing Calculator Application")
        self.logger.debug(f"Application environment: {EnvConfig.APP_ENV}")
        
        self.commands: Dict[str, Command] = {}
        self.running = True
        
        # Register core commands
        self._register_core_commands()
        
        # Load plugin commands
        self._load_plugin_commands()
        
        # Register menu command (needs access to commands dictionary)
        self.commands['menu'] = MenuCommand(self.commands)
        
        self.logger.info("Calculator Application initialized successfully")
        
    def _register_core_commands(self) -> None:
        """Register core calculator commands"""
        self.logger.debug("Registering core commands")
        self.commands['add'] = AddCommand()
        self.commands['subtract'] = SubtractCommand()
        self.commands['multiply'] = MultiplyCommand()
        self.commands['divide'] = DivideCommand()
        self.commands['exit'] = ExitCommand()
        self.commands['quit'] = ExitCommand()
        self.logger.debug(f"Registered {len(self.commands)} core commands")
        
    def _load_plugin_commands(self) -> None:
        """Load and register plugin commands"""
        self.logger.debug("Loading plugin commands")
        plugin_manager = PluginManager()
        plugin_commands = plugin_manager.load_plugins()
        
        # Add all discovered plugin commands to the command registry
        self.commands.update(plugin_commands)
        
        # Log loaded plugins
        if plugin_commands:
            self.logger.info(f"Loaded {len(plugin_commands)} plugin commands: {', '.join(plugin_commands.keys())}")
        else:
            self.logger.info("No plugin commands were loaded")
    
    def execute_command(self, command_name: str, args: List[str]) -> Optional[str]:
        """
        Execute the specified command with given arguments
        Returns command result or None if command not found
        """
        command_name_lower = command_name.lower()
        command = self.commands.get(command_name_lower)
        
        if command is None:
            self.logger.warning(f"Unknown command attempted: {command_name}")
            return f"Unknown command: {command_name}. Type 'menu' to see available commands."
        
        try:
            self.logger.info(f"Executing command: {command_name_lower} with args: {args}")
            result = command.execute(*args)
            
            # If it's a calculation command, store in history
            if command_name_lower in ['add', 'subtract', 'multiply', 'divide']:
                # Convert string args to float
                float_args = [float(arg) for arg in args]
                if len(float_args) >= 2:
                    from calculator.calculator import Calculator
                    from calculator.calculation import Calculation
                    
                    # Create and store calculation in history
                    calculation = Calculator.create_calculation(
                        float_args[0], float_args[1], command_name_lower
                    )
                    Calculations.add_calculation(calculation)
                    self.logger.debug(f"Added calculation to history: {calculation}")
            
            # Check for exit command
            if isinstance(result, bool) and not result:
                self.logger.info("Exit command received")
                self.running = False
                return "Exiting calculator application. Goodbye!"
            
            self.logger.debug(f"Command result: {result}")
            return str(result)
            
        except ValueError as e:
            self.logger.error(f"ValueError during execution of {command_name_lower}: {e}")
            return f"Error: {e}"
        except ZeroDivisionError as e:
            self.logger.error(f"ZeroDivisionError during execution of {command_name_lower}: {e}")
            return f"Error: {e}"
        except Exception as e:
            self.logger.error(f"Unexpected error during execution of {command_name_lower}", exc_info=True)
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
        # Display welcome message with environment info
        print(f"Welcome to the Calculator Application! (Environment: {EnvConfig.APP_ENV})")
        print("Type 'menu' to see available commands or 'exit' to quit.")
        print("=" * 50)
        
        self.logger.info("Starting calculator REPL loop")
        
        # Show menu at startup
        print(self.execute_command('menu', []))
        
        # Check if advanced operations are enabled
        if EnvConfig.ENABLE_ADVANCED_OPERATIONS:
            print("Advanced operations are enabled.")
            self.logger.debug("Advanced operations are enabled via environment configuration")
        
        # Main REPL loop
        while self.running:
            try:
                # Read
                user_input = input("calculator> ")
                self.logger.debug(f"User input: {user_input}")
                
                # Parse
                command_name, args = self.parse_input(user_input)
                
                if not command_name:
                    continue
                
                # Evaluate and Print
                result = self.execute_command(command_name, args)
                print(result)
                
            except KeyboardInterrupt:
                self.logger.info("KeyboardInterrupt received, shutting down")
                print("\nExiting calculator application. Goodbye!")
                self.running = False
            except EOFError:
                self.logger.info("EOFError received, shutting down")
                print("\nExiting calculator application. Goodbye!")
                self.running = False
            except Exception as e:
                self.logger.error(f"Unexpected error in REPL loop: {e}", exc_info=True)
                print(f"Error: {e}")

def main():
    """Main entry point for the calculator application"""
    # Set up root logger
    logger = get_logger('calculator_app')
    
    # Log application startup
    logger.info("=== Calculator Application Starting ===")
    logger.info(f"Environment: {EnvConfig.APP_ENV}")
    
    try:
        app = CalculatorApp()
        app.run()
    except Exception as e:
        logger.critical(f"Unhandled exception in main: {e}", exc_info=True)
        print(f"Critical error: {e}")
        sys.exit(1)
    finally:
        logger.info("=== Calculator Application Shutdown ===")

if __name__ == "__main__":
    main()
