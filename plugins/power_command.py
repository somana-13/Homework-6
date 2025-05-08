"""
Sample plugin implementing a power command for the calculator
"""
from commands.command_interface import Command

class PowerCommand(Command):
    """Command class for calculating one number raised to the power of another"""
    
    def execute(self, *args, **kwargs) -> float:
        """Execute power operation with provided arguments"""
        if len(args) != 2:
            raise ValueError("Power command requires exactly 2 numeric arguments")
        
        # Convert string arguments to float
        base = float(args[0])
        exponent = float(args[1])
        
        # Calculate power
        return base ** exponent
    
    @property
    def description(self) -> str:
        """Return description of the power command"""
        return "Raise the first number to the power of the second number"
    
    @property
    def usage(self) -> str:
        """Return usage information for the power command"""
        return "power <base> <exponent>"
