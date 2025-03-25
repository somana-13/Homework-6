"""
Main module to demonstrate calculator functionality
"""
import sys
from calculator.calculator import Calculator
from calculator.calculation import Calculation
from calculator.calculations import Calculations

def main():
    """Main function to demonstrate calculator functionality"""
    if len(sys.argv) == 4:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            operation = sys.argv[3]

            if operation == "add":
                result = Calculator.add(a, b)
            elif operation == "subtract":
                result = Calculator.subtract(a, b)
            elif operation == "multiply":
                result = Calculator.multiply(a, b)
            elif operation == "divide":
                if b == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = Calculator.divide(a, b)
            else:
                print(f"Unknown operation: {operation}")
                return

            print(f"The result of {a} {operation} {b} is equal to {result}")

        except ValueError:
            print("Invalid input: Please enter valid numbers.")
        except ZeroDivisionError as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    else:
        print("Usage: python main.py <num1> <num2> <operation>")
        sys.exit(1)

if __name__ == "__main__":
    main()
