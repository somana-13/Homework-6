"""
Main module to demonstrate calculator functionality
"""
from calculator.calculator import Calculator
from calculator.calculation import Calculation
from calculator.calculations import Calculations

def main():
    """Main function to demonstrate calculator functionality"""
    
    print("Calculator Demo")
    print("--------------")
    
    # Perform calculations using static methods
    a, b = 10, 5
    print(f"Addition: {a} + {b} = {Calculator.add(a, b)}")
    print(f"Subtraction: {a} - {b} = {Calculator.subtract(a, b)}")
    print(f"Multiplication: {a} × {b} = {Calculator.multiply(a, b)}")
    print(f"Division: {a} ÷ {b} = {Calculator.divide(a, b)}")
    
    # Create and store calculations
    add_calc = Calculator.create_calculation(a, b, "add")
    Calculations.add_calculation(add_calc)
    
    subtract_calc = Calculator.create_calculation(a, b, "subtract")
    Calculations.add_calculation(subtract_calc)
    
    multiply_calc = Calculator.create_calculation(a, b, "multiply")
    Calculations.add_calculation(multiply_calc)
    
    divide_calc = Calculator.create_calculation(a, b, "divide")
    Calculations.add_calculation(divide_calc)
    
    # Perform the calculations
    print("\nPerforming stored calculations:")
    for calc in Calculations.get_history():
        result = calc.perform()
        print(f"{calc.a} {calc.operation} {calc.b} = {result}")
    
    # Get the latest calculation
    latest = Calculations.get_latest()
    print(f"\nLatest calculation: {latest}")
    
    # Find calculations by operation
    add_calcs = Calculations.find_by_operation("add")
    print(f"\nFound {len(add_calcs)} addition operations in history")
    
    # Try to divide by zero
    try:
        Calculator.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"\nHandled exception: {e}")

if __name__ == "__main__":
    main()