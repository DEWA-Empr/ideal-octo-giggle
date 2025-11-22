"""
Finance Budget Application
A simple application to track and manage income budgets on daily, monthly, and yearly basis.
"""

from datetime import date
from typing import Dict, Optional
import json


class BudgetTracker:
    """Track income and budgets across different time periods"""
    
    def __init__(self):
        self.daily_budget: Dict[str, float] = {}
        self.monthly_budget: Dict[str, float] = {}
        self.yearly_budget: Dict[str, float] = {}
        
    def add_daily_income(self, amount: float, date_str: Optional[str] = None) -> None:
        """Add income for a specific day"""
        if date_str is None:
            date_str = date.today().strftime("%Y-%m-%d")
        
        if amount < 0:
            raise ValueError("Income amount must be positive")
        
        if date_str in self.daily_budget:
            self.daily_budget[date_str] += amount
        else:
            self.daily_budget[date_str] = amount
    
    def add_monthly_income(self, amount: float, month_str: Optional[str] = None) -> None:
        """Add income for a specific month (format: YYYY-MM)"""
        if month_str is None:
            month_str = date.today().strftime("%Y-%m")
        
        if amount < 0:
            raise ValueError("Income amount must be positive")
        
        if month_str in self.monthly_budget:
            self.monthly_budget[month_str] += amount
        else:
            self.monthly_budget[month_str] = amount
    
    def add_yearly_income(self, amount: float, year_str: Optional[str] = None) -> None:
        """Add income for a specific year (format: YYYY)"""
        if year_str is None:
            year_str = str(date.today().year)
        
        if amount < 0:
            raise ValueError("Income amount must be positive")
        
        if year_str in self.yearly_budget:
            self.yearly_budget[year_str] += amount
        else:
            self.yearly_budget[year_str] = amount
    
    def get_daily_budget(self, date_str: Optional[str] = None) -> float:
        """Get budget for a specific day"""
        if date_str is None:
            date_str = date.today().strftime("%Y-%m-%d")
        return self.daily_budget.get(date_str, 0.0)
    
    def get_monthly_budget(self, month_str: Optional[str] = None) -> float:
        """Get budget for a specific month"""
        if month_str is None:
            month_str = date.today().strftime("%Y-%m")
        return self.monthly_budget.get(month_str, 0.0)
    
    def get_yearly_budget(self, year_str: Optional[str] = None) -> float:
        """Get budget for a specific year"""
        if year_str is None:
            year_str = str(date.today().year)
        return self.yearly_budget.get(year_str, 0.0)
    
    def get_all_daily_budgets(self) -> Dict[str, float]:
        """Get all daily budgets"""
        return dict(sorted(self.daily_budget.items()))
    
    def get_all_monthly_budgets(self) -> Dict[str, float]:
        """Get all monthly budgets"""
        return dict(sorted(self.monthly_budget.items()))
    
    def get_all_yearly_budgets(self) -> Dict[str, float]:
        """Get all yearly budgets"""
        return dict(sorted(self.yearly_budget.items()))
    
    def save_to_file(self, filename: str) -> None:
        """Save budget data to a JSON file"""
        data = {
            'daily': self.daily_budget,
            'monthly': self.monthly_budget,
            'yearly': self.yearly_budget
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename: str) -> None:
        """Load budget data from a JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.daily_budget = data.get('daily', {})
                self.monthly_budget = data.get('monthly', {})
                self.yearly_budget = data.get('yearly', {})
        except FileNotFoundError:
            pass
    
    def get_summary(self) -> str:
        """Get a summary of all budgets"""
        lines = ["=== Budget Summary ===\n"]
        
        lines.append("Daily Budgets:")
        if self.daily_budget:
            for date_str, amount in sorted(self.daily_budget.items()):
                lines.append(f"  {date_str}: ${amount:.2f}")
        else:
            lines.append("  No daily budgets recorded")
        
        lines.append("\nMonthly Budgets:")
        if self.monthly_budget:
            for month_str, amount in sorted(self.monthly_budget.items()):
                lines.append(f"  {month_str}: ${amount:.2f}")
        else:
            lines.append("  No monthly budgets recorded")
        
        lines.append("\nYearly Budgets:")
        if self.yearly_budget:
            for year_str, amount in sorted(self.yearly_budget.items()):
                lines.append(f"  {year_str}: ${amount:.2f}")
        else:
            lines.append("  No yearly budgets recorded")
        
        return "\n".join(lines)
