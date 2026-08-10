from datetime import datetime

def get_valid_int(prompt, allow_negative=True, min_value=None):
    """Keep asking for value untill condition satifies"""
    while True:
        try:
            value = int(input(prompt))
            if not allow_negative and value < 0:
                print("Invalid input: value cannot be negative!")
                continue
            elif min_value is not None and value < min_value:
                print(f"Invalid input: value cannot be less than {min_value}!")
                continue
            return value
        except ValueError:
            print("Invalid input: please enter a whole number.")


def get_non_empty_input(prompt):
    """Keep asking for input untill condition satisfied"""

    while True:
        value = input(prompt)
        if value:
            return value
        print("Input cannot be empty. Please Try again")


def get_valid_date(prompt):
    while True:
        value = input(prompt)
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD format (e.g. 2025-01-15).")