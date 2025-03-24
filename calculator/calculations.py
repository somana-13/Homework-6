"""
Calculations module for managing calculation history
"""
from typing import List, Optional
from calculator.calculation import Calculation

class Calculations:
    """
    Calculations class for managing a history of calculations
    """
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        """Add a calculation to the history"""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Get the complete calculation history"""
        return cls.history.copy()

    @classmethod
    def clear_history(cls) -> None:
        """Clear the calculation history"""
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Optional[Calculation]:
        """Get the most recent calculation or None if history is empty"""
        if cls.history:
            return cls.history[-1]
        return None
    
    @classmethod
    def find_by_operation(cls, operation: str) -> List[Calculation]:
        """Find all calculations with the specified operation"""
        return [calc for calc in cls.history if calc.operation == operation]