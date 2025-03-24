"""
Tests for the Calculator class
"""
import pytest
from calculator.calculator import Calculator

class TestCalculator:
    """Test cases for Calculator class"""

    def test_add(self):
        """Test addition functionality"""
        assert Calculator.add(2, 2) == 4
        assert Calculator.add(-1, 1) == 0
        assert Calculator.add(2.5, 3.5) == 6.0

    def test_subtract(self):
        """Test subtraction functionality"""
        assert Calculator.subtract(5, 3) == 2
        assert Calculator.subtract(1, 5) == -4
        assert Calculator.subtract(10.5, 0.5) == 10.0

    def test_multiply(self):
        """Test multiplication functionality"""
        assert Calculator.multiply(3, 4) == 12
        assert Calculator.multiply(-2, 3) == -6
        assert Calculator.multiply(2.5, 4) == 10.0

    def test_divide(self):
        """Test division functionality"""
        assert Calculator.divide(10, 2) == 5
        assert Calculator.divide(7, 2) == 3.5
        assert Calculator.divide(-10, 5) == -2

    def test_divide_by_zero(self):
        """Test that divide by zero raises appropriate exception"""
        with pytest.raises(ZeroDivisionError):
            Calculator.divide(5, 0)

    def test_create_calculation(self):
        """Test creation of Calculation objects"""
        calc = Calculator.create_calculation(5, 2, "add")
        assert calc.a == 5
        assert calc.b == 2
        assert calc.operation == "add"