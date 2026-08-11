import finance_manager
from utils import get_non_empty_input


def show_menu():
    print("\n========== Personal Finance Manager =========")
    print("1. Add Income")

    print("2. Add Expense")

    print("3. View Transactions")

    print("4. Search Transactions")

    print("5. Update Transaction")

    print("6. Delete Transaction")

    print("7. Exit")


while True:
    show_menu()
    choice = get_non_empty_input("Choice: ")

    if choice == "1":
        finance_manager.add_income()
    elif choice == "2":
        finance_manager.add_expense()
    elif choice == "3":
        finance_manager.view_transactions()
    elif choice == "4":
        finance_manager.search_transactions()
    # elif choice == "5":
    #         employee_manager.delete_employee()
    elif choice == "6":
        finance_manager.delete_transaction()
    elif choice == "7":
        print("Goodbye!")
        break
