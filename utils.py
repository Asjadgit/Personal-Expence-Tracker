from datetime import datetime
import json

DATA_FILE = "expenses.json"

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
        value = input(prompt).strip()
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

def save_transactions(transactions):
    """ Save Each Transactions into the json file in json format """
    data = [trans.to_dict() for trans in transactions]
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_transactions():
    """ Load All Transactions from the json file into the class as loads """
    from finance import Finance

    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []
    return [Finance.from_dict(item) for item in data]