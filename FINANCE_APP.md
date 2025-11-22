# Finance Budget Application

A simple Python application for users to budget their income on daily, monthly, and yearly basis.

## Features

- **Daily Budget Tracking**: Record and track income for specific days
- **Monthly Budget Tracking**: Record and track income for specific months
- **Yearly Budget Tracking**: Record and track income for specific years
- **Data Persistence**: Save and load budget data to/from JSON files
- **Interactive CLI**: User-friendly command-line interface
- **Comprehensive Summaries**: View all budgets at a glance

## Installation

No installation required! Just ensure you have Python 3.6+ installed on your system.

## Usage

### Running the Application

```bash
python3 main.py
```

### Menu Options

The application provides an interactive menu with the following options:

1. **Add Daily Income** - Record income for a specific day
2. **Add Monthly Income** - Record income for a specific month
3. **Add Yearly Income** - Record income for a specific year
4. **View Daily Budget** - Check budget for a specific day
5. **View Monthly Budget** - Check budget for a specific month
6. **View Yearly Budget** - Check budget for a specific year
7. **View All Budgets** - Display all recorded budgets
8. **View Summary** - Show a comprehensive summary of all budgets
9. **Save Budget Data** - Manually save data to file
10. **Load Budget Data** - Manually load data from file
0. **Exit** - Exit the application (automatically saves data)

### Example Usage

#### Adding Daily Income
```
Enter your choice (0-10): 1

--- Add Daily Income ---
Enter income amount: $50.25
Enter date (YYYY-MM-DD) or press Enter for today: 2025-01-15
✓ Added $50.25 to daily income for 2025-01-15
```

#### Adding Monthly Income
```
Enter your choice (0-10): 2

--- Add Monthly Income ---
Enter income amount: $3500
Enter month (YYYY-MM) or press Enter for current month: 2025-01
✓ Added $3500.00 to monthly income for 2025-01
```

#### Adding Yearly Income
```
Enter your choice (0-10): 3

--- Add Yearly Income ---
Enter income amount: $60000
Enter year (YYYY) or press Enter for current year: 2025
✓ Added $60000.00 to yearly income for 2025
```

#### Viewing Summary
```
Enter your choice (0-10): 8

=== Budget Summary ===

Daily Budgets:
  2025-01-15: $50.25
  2025-01-16: $75.00

Monthly Budgets:
  2025-01: $3500.00
  2025-02: $3700.00

Yearly Budgets:
  2025: $60000.00
```

## Using as a Python Module

You can also use the `BudgetTracker` class directly in your Python code:

```python
from budget import BudgetTracker

# Create a tracker instance
tracker = BudgetTracker()

# Add income
tracker.add_daily_income(100.0, "2025-01-15")
tracker.add_monthly_income(3000.0, "2025-01")
tracker.add_yearly_income(50000.0, "2025")

# Get budgets
daily_budget = tracker.get_daily_budget("2025-01-15")
monthly_budget = tracker.get_monthly_budget("2025-01")
yearly_budget = tracker.get_yearly_budget("2025")

# Get all budgets
all_daily = tracker.get_all_daily_budgets()
all_monthly = tracker.get_all_monthly_budgets()
all_yearly = tracker.get_all_yearly_budgets()

# Save and load data
tracker.save_to_file("my_budget.json")
tracker.load_from_file("my_budget.json")

# Get summary
print(tracker.get_summary())
```

## Data Storage

Budget data is automatically saved to `budget_data.json` in the application directory. The file uses JSON format for easy portability and readability.

Example data file:
```json
{
  "daily": {
    "2025-01-15": 100.0,
    "2025-01-16": 150.0
  },
  "monthly": {
    "2025-01": 3000.0,
    "2025-02": 3500.0
  },
  "yearly": {
    "2025": 50000.0
  }
}
```

## Running Tests

To run the unit tests:

```bash
python3 test_budget.py
```

For verbose output:

```bash
python3 test_budget.py -v
```

## Features in Detail

### Input Validation

- All income amounts must be positive numbers
- Negative values will trigger an error message
- Invalid date formats are handled gracefully

### Default Values

- If no date is specified for daily income, today's date is used
- If no month is specified for monthly income, the current month is used
- If no year is specified for yearly income, the current year is used

### Cumulative Budgets

- Multiple income entries for the same period are automatically summed
- Example: Adding $100 and $50 on the same day results in a $150 daily budget

### Auto-Save

- Data is automatically saved when you exit the application
- You can also manually save at any time using option 9

## Requirements

- Python 3.6 or higher
- No external dependencies required

## License

MIT License - See LICENSE file for details

## Contributing

Feel free to submit issues or pull requests to improve the application!
