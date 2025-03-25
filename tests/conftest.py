import pytest
from faker import Faker
import random

# Create a Faker instance
faker = Faker()

# Add command-line option for the number of records
def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of records to generate")

@pytest.fixture(scope="session")
def num_records(request):
    return request.config.getoption("--num_records")

# Generate fake test data
@pytest.fixture(scope="function")
def fake_test_data():
    a = faker.random_int(min=1, max=100)
    b = faker.random_int(min=1, max=100)
    operation = random.choice(['add', 'subtract', 'multiply', 'divide'])
    
    # Calculate expected result
    if operation == 'add':
        expected = f"The result of {a} add {b} is equal to {a + b}"
    elif operation == 'subtract':
        expected = f"The result of {a} subtract {b} is equal to {a - b}"
    elif operation == 'multiply':
        expected = f"The result of {a} multiply {b} is equal to {a * b}"
    elif operation == 'divide':
        expected = f"The result of {a} divide {b} is equal to {a / b}" if b != 0 else "An error occurred: Cannot divide by zero"
    else:
        expected = f"Unknown operation: {operation}"

    return a, b, operation, expected
