# Personal Finance Manager

A command-line personal finance tracker built in Python. Add, search, update, delete, and summarize your income and expense transactions — all saved locally to a JSON file so your data persists between runs.

## Features

- **Add Income / Add Expense** — record transactions with ID, category, description, date, and amount
- **View Transactions** — list every saved transaction
- **Search Transactions** — search by Transaction ID, Category, Description, or Type (case-insensitive text search)
- **Update Transaction** — edit the amount, category, description, or date of an existing transaction
- **Delete Transaction** — remove a transaction, with a confirmation prompt before deleting
- **Financial Summary** — total income, total expense, balance, highest/lowest expense, and savings rate
- **Category Summary** — total amount spent per category
- **Persistent storage** — all transactions are saved to and loaded from a local JSON file, so data survives program restarts

## Project Structure

```
Personal Expense Tracker/
├── main.py              # Entry point — menu loop and user interaction
├── finance_manager.py   # Core feature functions (add, view, search, update, delete, summaries)
├── finance.py           # Finance class — represents a single transaction
├── utils.py             # Reusable input-validation helpers and file I/O (save/load)
└── transactions.json    # Auto-generated data file storing saved transactions
```

## Requirements

- Python 3.8 or higher (no external dependencies — uses only the standard library)

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/Asjadgit/Personal-Expence-Tracker
   cd Personal-Expence-Tracker
   ```

2. Run the program:
   ```
   python main.py
   ```

3. Use the on-screen menu to manage your transactions:
   ```
   ========== Personal Finance Manager ==========
   1. Add Income
   2. Add Expense
   3. View Transactions
   4. Search Transactions
   5. Update Transaction
   6. Delete Transaction
   7. Financial Summary
   8. Category Summary
   9. Save & Exit
   ```

## How It Works

### The `Finance` class (`finance.py`)
Each transaction is represented as a `Finance` object with the following fields:

| Field | Description |
|---|---|
| `transaction_id` | Unique integer identifier |
| `transaction_type` | `"income"` or `"expense"` |
| `transactionamount` | Numeric amount (validated — must be greater than zero) |
| `transaction_category` | e.g. `"Food"`, `"Salary"`, `"Rent"` |
| `transaction_description` | Free-text description |
| `transaction_date` | Date in `YYYY-MM-DD` format (validated) |

Amount and date use Python properties with setters that validate input and raise `ValueError` on invalid data (negative/zero amounts, malformed dates), so bad data can never be silently stored.

### Data persistence (`utils.py`)
- `save_transactions(transactions)` — converts each `Finance` object to a dictionary via `to_dict()` and writes the full list to `transactions.json`
- `load_transactions()` — reads `transactions.json`, and rebuilds each entry back into a real `Finance` object via `from_dict()`, so all validation and methods are available again after loading

### Input validation (`utils.py`)
Reusable helper functions ensure the user can't proceed with bad input:
- `get_non_empty_input(prompt)` — rejects blank input
- `get_valid_int(prompt, allow_negative, min_value)` — rejects non-numeric or out-of-range input
- `get_valid_date(prompt)` — rejects anything that doesn't match `YYYY-MM-DD`

## Example Session

```
Choice: 1

 Enter Your Transaction Details

Enter transaction Id: 1
Enter transaction category: Salary
Enter transaction Description: July paycheck
Enter transaction date: 2025-07-01
Enter transaction amount: 90000
Transaction with id 1 added successfully.

Choice: 7
========== Financial Summary ==========
Total Transactions  : 5
Total Income        : 90000
Total Expense       : 2500
Balance             : 87500
Highest Expense     : 1000
Lowest Expense      : 600
Savings Rate        : 97.22%
```

## Roadmap / Possible Future Improvements

- Restrict categories to a predefined list per transaction type (e.g. Income → Salary, Freelance; Expense → Food, Rent, Transport)
- Export summaries to CSV
- Filter transactions by date range
- Add unit tests for `Finance` class validation and `finance_manager` functions

## License

This project is open source and available for personal or educational use.
