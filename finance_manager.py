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

def update_transaction():
    print("\nEnter Transaction Id to update: ")
    found = False
    
    transaction_id = get_valid_int("Enter Here: ")
    for trans in transactions:
        if transaction_id == trans.transaction_id:
            found = True
            print("Transaction Found! Displayed Below")
            trans.display_transaction()

            print("What would you like to update: \n")
            print("1. Amount")
            print("2. Category")
            print("3. Description")
            print("4. Date")

            choice = get_non_empty_input("Choice: ")
            
            if choice == "1":
                while True:
                    try:
                        new_transaction_amount   = int(input("Enter transaction amount: "))
                        trans.transactionamount  = new_transaction_amount
                        break
                    except ValueError as error:
                        print("Invalid Input: Must be numeric")
                    # transactions.append(trans) 
                print(f"Transaction with id {trans.transaction_id} updated successfully.")
            elif choice == "2":
                new_transaction_category      = get_non_empty_input("Enter transaction category: ")
                trans.transaction_category    = new_transaction_category
                print(f"Transaction with id {trans.transaction_id} updated successfully.")
            elif choice == "3":
                new_transaction_description   = get_non_empty_input("Enter transaction description: ")
                trans.transaction_description = new_transaction_description
                print(f"Transaction with id {trans.transaction_id} updated successfully.")
            elif choice == "4":
                new_transaction_date          = get_valid_date("Enter transaction date: ")
                trans.transaction_date        = new_transaction_date
                print(f"Transaction with id {trans.transaction_id} updated successfully.")
            else:
                print("Invalid choice.\n")

            trans.display_transaction()
            save_transactions(transactions)

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