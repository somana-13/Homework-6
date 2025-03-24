"""
Tests for the Calculations class
"""
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations

class TestCalculations:
    """Test cases for Calculations class"""
    
    @pytest.fixture
    def setup_calculations(self):
        """Fixture to set up test data and clear history"""
        # Clear any existing history before each test
        Calculations.clear_history()
        
        # Create test calculations
        add_calc = Calculation(2, 2, 'add')
        subtract_calc = Calculation(10, 5, 'subtract')
        multiply_calc = Calculation(3, 4, 'multiply')
        divide_calc = Calculation(20, 5, 'divide')
        
        return {
            'add': add_calc,
            'subtract': subtract_calc,
            'multiply': multiply_calc,
            'divide': divide_calc
        }
    
    def test_add_calculation(self, setup_calculations):
        """Test adding a calculation to history"""
        calc = setup_calculations['add']
        Calculations.add_calculation(calc)
        assert len(Calculations.get_history()) == 1
        assert Calculations.get_history()[0] == calc
    
    def test_add_multiple_calculations(self, setup_calculations):
        """Test adding multiple calculations"""
        for calc in setup_calculations.values():
            Calculations.add_calculation(calc)
        
        assert len(Calculations.get_history()) == 4
    
    def test_get_history(self, setup_calculations):
        """Test getting calculation history"""
        # Add two calculations
        Calculations.add_calculation(setup_calculations['add'])
        Calculations.add_calculation(setup_calculations['subtract'])
        
        history = Calculations.get_history()
        assert len(history) == 2
        assert history[0] == setup_calculations['add']
        assert history[1] == setup_calculations['subtract']
    
    def test_clear_history(self, setup_calculations):
        """Test clearing calculation history"""
        # Add calculations
        for calc in setup_calculations.values():
            Calculations.add_calculation(calc)
        
        # Clear history
        Calculations.clear_history()
        assert len(Calculations.get_history()) == 0
    
    def test_get_latest(self, setup_calculations):
        """Test getting the latest calculation"""
        # Empty history should return None
        assert Calculations.get_latest() is None
        
        # Add calculations and check latest
        Calculations.add_calculation(setup_calculations['add'])
        assert Calculations.get_latest() == setup_calculations['add']
        
        Calculations.add_calculation(setup_calculations['subtract'])
        assert Calculations.get_latest() == setup_calculations['subtract']
    
    def test_find_by_operation(self, setup_calculations):
        """Test finding calculations by operation"""
        # Add multiple calculations of different types
        for calc in setup_calculations.values():
            Calculations.add_calculation(calc)
        
        # Add another add calculation
        second_add = Calculation(3, 3, 'add')
        Calculations.add_calculation(second_add)
        
        # Test finding all add operations
        add_operations = Calculations.find_by_operation('add')
        assert len(add_operations) == 2
        assert setup_calculations['add'] in add_operations
        assert second_add in add_operations
        
        # Test finding subtract operations
        subtract_operations = Calculations.find_by_operation('subtract')
        assert len(subtract_operations) == 1
        assert setup_calculations['subtract'] in subtract_operations
        
        # Test finding non-existent operations
        power_operations = Calculations.find_by_operation('power')
        assert len(power_operations) == 0