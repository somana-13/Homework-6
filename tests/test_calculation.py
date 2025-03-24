"""
Tests for the Calculation class
"""
import pytest
from calculator.calculation import Calculation

class TestCalculation:
    """Test cases for Calculation class"""
    
    @pytest.fixture
    def setup_calculations(self):
        """Fixture to set up test calculations"""
        return {
            'add': Calculation(5, 3, 'add'),
            'subtract': Calculation(10, 4, 'subtract'),
            'multiply': Calculation(3, 7, 'multiply'),
            'divide': Calculation(15, 3, 'divide'),
            'divide_zero': Calculation(8, 0, 'divide'),
            'invalid': Calculation(1, 1, 'invalid_op')
        }
    
    def test_calculation_init(self, setup_calculations):
        """Test Calculation initialization"""
        calc = setup_calculations['add']
        assert calc.a == 5
        assert calc.b == 3
        assert calc.operation == 'add'
    
    def test_calculation_repr(self, setup_calculations):
        """Test string representation"""
        calc = setup_calculations['add']
        assert repr(calc) == "Calculation(5, 3, add)"
    
    def test_perform_add(self, setup_calculations):
        """Test add operation"""
        assert setup_calculations['add'].perform() == 8
    
    def test_perform_subtract(self, setup_calculations):
        """Test subtract operation"""
        assert setup_calculations['subtract'].perform() == 6
    
    def test_perform_multiply(self, setup_calculations):
        """Test multiply operation"""
        assert setup_calculations['multiply'].perform() == 21
    
    def test_perform_divide(self, setup_calculations):
        """Test divide operation"""
        assert setup_calculations['divide'].perform() == 5
    
    def test_perform_divide_by_zero(self, setup_calculations):
        """Test division by zero raises exception"""
        with pytest.raises(ZeroDivisionError):
            setup_calculations['divide_zero'].perform()
    
    def test_perform_invalid_operation(self, setup_calculations):
        """Test invalid operation raises exception"""
        with pytest.raises(ValueError):
            setup_calculations['invalid'].perform()