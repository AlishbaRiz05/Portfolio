"""Console Calculator - Alishba Rizwan
A simple menu-driven calculator with input validation."""

import math


def get_number(prompt):
    """Keep asking until the user types a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate(choice, a, b=None):
    """Return the result of the chosen operation."""
    if choice == "1":
        return a + b
    if choice == "2":
        return a - b
    if choice == "3":
        return a * b
    if choice == "4":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    if choice == "5":
        return a ** b
    if choice == "6":
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(a)


def show_menu():
    print("\n=== Console Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square root")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (0-6): ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Invalid option. Please choose from 0 to 6.")
            continue

        a = get_number("Enter the first number: ")
        b = None
        if choice != "6":                      # square root needs one number only
            b = get_number("Enter the second number: ")

        try:
            result = calculate(choice, a, b)
            print(f"Result: {result:g}")
        except (ZeroDivisionError, ValueError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
