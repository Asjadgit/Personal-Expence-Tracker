import finance
from utils import get_non_empty_input, get_valid_int, get_valid_date

def add_transaction_details():
    print("\n Enter Your Transaction Details\n")
    transaction_id            = get_valid_int("Enter transaction Id: ", allow_negative=False)
    transaction_type          = get_non_empty_input("Enter transaction type: ")
    transaction_category      = get_non_empty_input("Enter transaction category: ")
    transaction_description   = get_non_empty_input("Enter transaction Description: " )
    transaction_date          = get_valid_date("Enter transaction date: ")

    while True:
        try:
            transaction_amount   = int(input("Enter transaction amount: "))
            transaction = finance.Finance(transaction_id, transaction_type, transaction_amount, transaction_category, transaction_description, transaction_date)
            break
        except ValueError as error:
            print("Invalid Input: Must be numeric")

    transaction.display_transaction()
    
add_transaction_details()