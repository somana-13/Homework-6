"""
Calculator module providing static methods for arithmetic operations
"""
from typing import TypeVar, Generic
from calculator.calculation import Calculation

T = TypeVar('T', int, float)

class Calculator:
    """
    Calculator class providing static methods for basic arithmetic operations
    """
    @staticmethod
    def add(a: T, b: T) -> T:
        """Add two numbers and return the result"""
        return a + b

    @staticmethod
    def subtract(a: T, b: T) -> T:
        """Subtract b from a and return the result"""
        return a - b

    @staticmethod
    def multiply(a: T, b: T) -> T:
        """Multiply two numbers and return the result"""
        return a * b

    @staticmethod
    def divide(a: T, b: T) -> T:
        """
        Divide a by b and return the result
        Raises ZeroDivisionError if b is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    @staticmethod
    def create_calculation(a: T, b: T, operation: str) -> Calculation:
        """Create and return a Calculation object"""
        return Calculation(a, b, operation)