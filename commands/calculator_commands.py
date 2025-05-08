"""
Calculator Commands module implementing concrete command classes
"""
from typing import List, Any, Dict
from commands.command_interface import Command
from calculator.calculator import Calculator

class AddCommand(Command):
    """Command class for addition operation"""
    
    def execute(self, *args, **kwargs) -> float:
        """Execute addition operation with provided arguments"""
        if len(args) < 2:
            raise ValueError("Add command requires at least 2 numeric arguments")
        
        # Convert string arguments to float
        nums = [float(arg) for arg in args]
        result = nums[0]
        
        # Add the rest of the numbers to the first one
        for num in nums[1:]:
            result = Calculator.add(result, num)
            
        return result
    
    @property
    def description(self) -> str:
        """Return description of the add command"""
        return "Add two or more numbers together"
    
    @property
    def usage(self) -> str:
        """Return usage information for the add command"""
        return "add <number1> <number2> [number3 ...]"


class SubtractCommand(Command):
    """Command class for subtraction operation"""
    
    def execute(self, *args, **kwargs) -> float:
        """Execute subtraction operation with provided arguments"""
        if len(args) < 2:
            raise ValueError("Subtract command requires at least 2 numeric arguments")
        
        # Convert string arguments to float
        nums = [float(arg) for arg in args]
        result = nums[0]
        
        # Subtract the rest of the numbers from the first one
        for num in nums[1:]:
            result = Calculator.subtract(result, num)
            
        return result
    
    @property
    def description(self) -> str:
        """Return description of the subtract command"""
        return "Subtract numbers from the first number"
    
    @property
    def usage(self) -> str:
        """Return usage information for the subtract command"""
        return "subtract <number1> <number2> [number3 ...]"


class MultiplyCommand(Command):
    """Command class for multiplication operation"""
    
    def execute(self, *args, **kwargs) -> float:
        """Execute multiplication operation with provided arguments"""
        if len(args) < 2:
            raise ValueError("Multiply command requires at least 2 numeric arguments")
        
        # Convert string arguments to float
        nums = [float(arg) for arg in args]
        result = nums[0]
        
        # Multiply the rest of the numbers with the first one
        for num in nums[1:]:
            result = Calculator.multiply(result, num)
            
        return result
    
    @property
    def description(self) -> str:
        """Return description of the multiply command"""
        return "Multiply two or more numbers together"
    
    @property
    def usage(self) -> str:
        """Return usage information for the multiply command"""
        return "multiply <number1> <number2> [number3 ...]"


class DivideCommand(Command):
    """Command class for division operation"""
    
    def execute(self, *args, **kwargs) -> float:
        """Execute division operation with provided arguments"""
        if len(args) < 2:
            raise ValueError("Divide command requires at least 2 numeric arguments")
        
        # Convert string arguments to float
        nums = [float(arg) for arg in args]
        result = nums[0]
        
        # Divide the first number by the rest of the numbers
        for num in nums[1:]:
            result = Calculator.divide(result, num)
            
        return result
    
    @property
    def description(self) -> str:
        """Return description of the divide command"""
        return "Divide the first number by the rest of the numbers"
    
    @property
    def usage(self) -> str:
        """Return usage information for the divide command"""
        return "divide <number1> <number2> [number3 ...]"


class MenuCommand(Command):
    """Command class to display available commands"""
    
    def __init__(self, command_registry: Dict[str, Command]):
        """Initialize MenuCommand with the command registry"""
        self.command_registry = command_registry
    
    def execute(self, *args, **kwargs) -> str:
        """
        Execute the menu command to display available commands
        Returns a formatted string with command information
        """
        result = "Available Commands:\n"
        result += "=" * 40 + "\n"
        
        # Sort commands alphabetically for better display
        sorted_commands = sorted(self.command_registry.items())
        
        for name, command in sorted_commands:
            result += f"{name.ljust(15)} - {command.description}\n"
            result += f"{'Usage:'.ljust(15)} {command.usage}\n"
            result += "-" * 40 + "\n"
            
        return result
    
    @property
    def description(self) -> str:
        """Return description of the menu command"""
        return "Display available commands and their usage"
    
    @property
    def usage(self) -> str:
        """Return usage information for the menu command"""
        return "menu"


class ExitCommand(Command):
    """Command class to exit the application"""
    
    def execute(self, *args, **kwargs) -> bool:
        """Execute the exit command"""
        return False  # Return False to signal exit from REPL loop
    
    @property
    def description(self) -> str:
        """Return description of the exit command"""
        return "Exit the calculator application"
    
    @property
    def usage(self) -> str:
        """Return usage information for the exit command"""
        return "exit"
