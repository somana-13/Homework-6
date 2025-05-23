import pytest
from calculator.calculator import Calculator

@pytest.mark.parametrize("a, b, operation, expected", [
    (5, 3, 'add', 8),
    (10, 2, 'subtract', 8),
    (4, 5, 'multiply', 20),
    (20, 4, 'divide', 5),
    (1, 0, 'divide', "Cannot divide by zero")
])
def test_static_calculations(a, b, operation, expected):
    """Test static calculation methods with fixed values"""
    if operation == 'add':
        assert Calculator.add(a, b) == expected
    elif operation == 'subtract':
        assert Calculator.subtract(a, b) == expected
    elif operation == 'multiply':
        assert Calculator.multiply(a, b) == expected
    elif operation == 'divide':
        if b != 0:
            assert Calculator.divide(a, b) == expected
        else:
            # Test that division by zero raises the correct exception
            with pytest.raises(ZeroDivisionError) as excinfo:
                Calculator.divide(a, b)
            assert "Cannot divide by zero" in str(excinfo.value)

def test_with_fake_data(fake_test_data):
    """Test calculator with Faker-generated random data"""
    a, b, operation, expected = fake_test_data
    
    # Extract just the numeric result if expected is a formatted string
    if isinstance(expected, str) and 'is equal to' in expected:
        # Parse the numeric result from the string
        expected_parts = expected.split('is equal to')
        if len(expected_parts) > 1:
            expected = float(expected_parts[1].strip())
    
    if operation == 'add':
        assert Calculator.add(a, b) == expected
    elif operation == 'subtract':
        assert Calculator.subtract(a, b) == expected
    elif operation == 'multiply':
        assert Calculator.multiply(a, b) == expected
    elif operation == 'divide':
        if b != 0:
            assert Calculator.divide(a, b) == expected
        else:
            # Test that division by zero raises the correct exception
            with pytest.raises(ZeroDivisionError) as excinfo:
                Calculator.divide(a, b)
            assert "Cannot divide by zero" in str(excinfo.value)
