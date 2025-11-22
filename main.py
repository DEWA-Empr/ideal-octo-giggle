#!/usr/bin/env python3
"""
Finance Budget Application - Main CLI Interface
"""

import sys
from datetime import date
from budget import BudgetTracker


def print_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("Finance Budget Application")
    print("="*50)
    print("1. Add Daily Income")
    print("2. Add Monthly Income")
    print("3. Add Yearly Income")
    print("4. View Daily Budget")
    print("5. View Monthly Budget")
    print("6. View Yearly Budget")
    print("7. View All Budgets")
    print("8. View Summary")
    print("9. Save Budget Data")
    print("10. Load Budget Data")
    print("0. Exit")
    print("="*50)


def get_float_input(prompt: str) -> float:
    """Get a valid float input from user"""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Amount must be positive. Please try again.")
                continue
            return value
        except ValueError:
            print("Error: Invalid number. Please try again.")


def get_string_input(prompt: str, allow_empty: bool = True) -> str:
    """Get a string input from user"""
    value = input(prompt).strip()
    if not allow_empty and not value:
        return None
    return value if value else None


def main():
    """Main application loop"""
    tracker = BudgetTracker()
    data_file = "budget_data.json"
    
    # Try to load existing data
    tracker.load_from_file(data_file)
    
    print("Welcome to Finance Budget Application!")
    print("Track your income daily, monthly, and yearly.")
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (0-10): ").strip()
        
        if choice == '1':
            # Add Daily Income
            print("\n--- Add Daily Income ---")
            amount = get_float_input("Enter income amount: $")
            date_str = get_string_input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            try:
                tracker.add_daily_income(amount, date_str)
                display_date = date_str if date_str else date.today().strftime("%Y-%m-%d")
                print(f"✓ Added ${amount:.2f} to daily income for {display_date}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            # Add Monthly Income
            print("\n--- Add Monthly Income ---")
            amount = get_float_input("Enter income amount: $")
            month_str = get_string_input("Enter month (YYYY-MM) or press Enter for current month: ")
            try:
                tracker.add_monthly_income(amount, month_str)
                display_month = month_str if month_str else date.today().strftime("%Y-%m")
                print(f"✓ Added ${amount:.2f} to monthly income for {display_month}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            # Add Yearly Income
            print("\n--- Add Yearly Income ---")
            amount = get_float_input("Enter income amount: $")
            year_str = get_string_input("Enter year (YYYY) or press Enter for current year: ")
            try:
                tracker.add_yearly_income(amount, year_str)
                display_year = year_str if year_str else str(date.today().year)
                print(f"✓ Added ${amount:.2f} to yearly income for {display_year}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '4':
            # View Daily Budget
            print("\n--- Daily Budget ---")
            date_str = get_string_input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            budget = tracker.get_daily_budget(date_str)
            display_date = date_str if date_str else date.today().strftime("%Y-%m-%d")
            print(f"Budget for {display_date}: ${budget:.2f}")
        
        elif choice == '5':
            # View Monthly Budget
            print("\n--- Monthly Budget ---")
            month_str = get_string_input("Enter month (YYYY-MM) or press Enter for current month: ")
            budget = tracker.get_monthly_budget(month_str)
            display_month = month_str if month_str else date.today().strftime("%Y-%m")
            print(f"Budget for {display_month}: ${budget:.2f}")
        
        elif choice == '6':
            # View Yearly Budget
            print("\n--- Yearly Budget ---")
            year_str = get_string_input("Enter year (YYYY) or press Enter for current year: ")
            budget = tracker.get_yearly_budget(year_str)
            display_year = year_str if year_str else str(date.today().year)
            print(f"Budget for {display_year}: ${budget:.2f}")
        
        elif choice == '7':
            # View All Budgets
            print("\n--- All Budgets ---")
            print("\nDaily Budgets:")
            daily = tracker.get_all_daily_budgets()
            if daily:
                for date_str, amount in daily.items():
                    print(f"  {date_str}: ${amount:.2f}")
            else:
                print("  No daily budgets recorded")
            
            print("\nMonthly Budgets:")
            monthly = tracker.get_all_monthly_budgets()
            if monthly:
                for month_str, amount in monthly.items():
                    print(f"  {month_str}: ${amount:.2f}")
            else:
                print("  No monthly budgets recorded")
            
            print("\nYearly Budgets:")
            yearly = tracker.get_all_yearly_budgets()
            if yearly:
                for year_str, amount in yearly.items():
                    print(f"  {year_str}: ${amount:.2f}")
            else:
                print("  No yearly budgets recorded")
        
        elif choice == '8':
            # View Summary
            print("\n" + tracker.get_summary())
        
        elif choice == '9':
            # Save Budget Data
            try:
                tracker.save_to_file(data_file)
                print(f"✓ Budget data saved to {data_file}")
            except Exception as e:
                print(f"Error saving data: {e}")
        
        elif choice == '10':
            # Load Budget Data
            try:
                tracker.load_from_file(data_file)
                print(f"✓ Budget data loaded from {data_file}")
            except Exception as e:
                print(f"Error loading data: {e}")
        
        elif choice == '0':
            # Exit
            print("\nSaving your data...")
            try:
                tracker.save_to_file(data_file)
                print("Thank you for using Finance Budget Application!")
            except Exception as e:
                print(f"Warning: Could not save data: {e}")
                print("Thank you for using Finance Budget Application!")
            print("Goodbye!")
            sys.exit(0)
        
        else:
            print("\nInvalid choice. Please enter a number between 0 and 10.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Exiting...")
        sys.exit(0)
