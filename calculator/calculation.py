"""
Calculation module for representing individual calculations
"""
from typing import TypeVar, Callable, Generic

T = TypeVar('T', int, float)

class Calculation(Generic[T]):
    """
    Calculation class represents a single calculation with two operands and an operation
    """
    def __init__(self, a: T, b: T, operation: str):
        """Initialize the calculation with operands and operation"""
        self.a = a
        self.b = b
        self.operation = operation

    def __repr__(self) -> str:
        """Return string representation of the calculation"""
        return f"Calculation({self.a}, {self.b}, {self.operation})"

    def perform(self) -> T:
        """
        Perform the stored calculation based on the operation
        Raises ValueError for unsupported operations
        """
        # Dictionary mapping operation symbols to corresponding functions
        operations = {
            'add': lambda: self.a + self.b,
            'subtract': lambda: self.a - self.b,
            'multiply': lambda: self.a * self.b,
            'divide': lambda: self._divide()
        }
        
        if self.operation not in operations:
            raise ValueError(f"Unsupported operation: {self.operation}")
        
        return operations[self.operation]()
    
    def _divide(self) -> T:
        """Helper method to handle division with zero check"""
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.a / self.b