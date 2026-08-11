import finance
from utils import get_non_empty_input, get_valid_int, get_valid_date, save_transactions, load_transactions

def add_income():
    add_transaction_details(transaction_type = "income")

def add_expense():
    add_transaction_details(transaction_type = "expense")

transactions = load_transactions()
def add_transaction_details(transaction_type):
    print("\n Enter Your Transaction Details\n")
    transaction_id            = get_valid_int("Enter transaction Id: ", allow_negative=False)
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
    transactions.append(transaction)
    save_transactions(transactions)
    print(f"Transaction with id {transaction.transaction_id} added successfully.")
    # transaction.display_transaction()

# add_transaction_details()

def view_transactions():
    if not transactions:
        print("No Transactions added yet")
        return
    for trans in transactions:
        trans.display_transaction()


def search_transactions():
    print("\nYou can search by: Transaction ID, Category, Description, Transaction type\n")
    query = get_non_empty_input("Enter to Search: ")

    found = False

    if query.isdigit():
        transaction_id = int(query)
        for trans in transactions:
            if transaction_id == trans.transaction_id:
                print("Transaction Found! Display Below")
                found = True
                trans.display_transaction()

    else:
        query = query.lower()
        for trans in transactions:
            if trans.transaction_category.lower() == query: 
                print("Transaction Found! Display Below")
                found = True
                trans.display_transaction()
            elif trans.transaction_description.lower() == query:
                print("Transaction Found! Display Below")
                found = True
                trans.display_transaction()
            elif trans.transaction_type.lower() == query:
                print("Transaction Found! Display Below")
                found = True
                trans.display_transaction()

    if not found:
        print("No Transaction Found!")


def delete_transaction():
    print("\nEnter Transaction Id to delete:\n")
    found = False

    transaction_id = get_valid_int("Enter Here: ")
    for trans in transactions:
        if transaction_id == trans.transaction_id:
            found = True
            print("Transaction Found! Display Below")
            trans.display_transaction()
            answer = get_non_empty_input("Do you really want to delete this transaction? (y/n): ").lower()
            if answer == 'y':
                transactions.remove(trans)
                save_transactions(transactions)
                print("Transaction Deleted Successfully!")
            else:
                print("Deletion Cancelled!")
            break

    if not found:
        print("No Transaction Found!")