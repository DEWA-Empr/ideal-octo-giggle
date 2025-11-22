"""
Unit tests for the Finance Budget Application
"""

import unittest
import os
import json
from datetime import date
from budget import BudgetTracker


class TestBudgetTracker(unittest.TestCase):
    """Test cases for BudgetTracker class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.tracker = BudgetTracker()
        self.test_file = "test_budget.json"
    
    def tearDown(self):
        """Clean up test files"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_daily_income_default_date(self):
        """Test adding daily income with default date"""
        self.tracker.add_daily_income(100.0)
        today = date.today().strftime("%Y-%m-%d")
        self.assertEqual(self.tracker.get_daily_budget(today), 100.0)
    
    def test_add_daily_income_specific_date(self):
        """Test adding daily income with specific date"""
        self.tracker.add_daily_income(150.0, "2025-01-15")
        self.assertEqual(self.tracker.get_daily_budget("2025-01-15"), 150.0)
    
    def test_add_daily_income_multiple(self):
        """Test adding multiple daily incomes to the same day"""
        self.tracker.add_daily_income(100.0, "2025-01-15")
        self.tracker.add_daily_income(50.0, "2025-01-15")
        self.assertEqual(self.tracker.get_daily_budget("2025-01-15"), 150.0)
    
    def test_add_daily_income_negative(self):
        """Test that negative daily income raises ValueError"""
        with self.assertRaises(ValueError):
            self.tracker.add_daily_income(-100.0)
    
    def test_add_monthly_income_default_month(self):
        """Test adding monthly income with default month"""
        self.tracker.add_monthly_income(3000.0)
        current_month = date.today().strftime("%Y-%m")
        self.assertEqual(self.tracker.get_monthly_budget(current_month), 3000.0)
    
    def test_add_monthly_income_specific_month(self):
        """Test adding monthly income with specific month"""
        self.tracker.add_monthly_income(3500.0, "2025-01")
        self.assertEqual(self.tracker.get_monthly_budget("2025-01"), 3500.0)
    
    def test_add_monthly_income_multiple(self):
        """Test adding multiple monthly incomes to the same month"""
        self.tracker.add_monthly_income(3000.0, "2025-01")
        self.tracker.add_monthly_income(500.0, "2025-01")
        self.assertEqual(self.tracker.get_monthly_budget("2025-01"), 3500.0)
    
    def test_add_monthly_income_negative(self):
        """Test that negative monthly income raises ValueError"""
        with self.assertRaises(ValueError):
            self.tracker.add_monthly_income(-1000.0)
    
    def test_add_yearly_income_default_year(self):
        """Test adding yearly income with default year"""
        self.tracker.add_yearly_income(50000.0)
        current_year = str(date.today().year)
        self.assertEqual(self.tracker.get_yearly_budget(current_year), 50000.0)
    
    def test_add_yearly_income_specific_year(self):
        """Test adding yearly income with specific year"""
        self.tracker.add_yearly_income(60000.0, "2025")
        self.assertEqual(self.tracker.get_yearly_budget("2025"), 60000.0)
    
    def test_add_yearly_income_multiple(self):
        """Test adding multiple yearly incomes to the same year"""
        self.tracker.add_yearly_income(50000.0, "2025")
        self.tracker.add_yearly_income(10000.0, "2025")
        self.assertEqual(self.tracker.get_yearly_budget("2025"), 60000.0)
    
    def test_add_yearly_income_negative(self):
        """Test that negative yearly income raises ValueError"""
        with self.assertRaises(ValueError):
            self.tracker.add_yearly_income(-5000.0)
    
    def test_get_daily_budget_nonexistent(self):
        """Test getting budget for a day with no income"""
        self.assertEqual(self.tracker.get_daily_budget("2025-01-15"), 0.0)
    
    def test_get_monthly_budget_nonexistent(self):
        """Test getting budget for a month with no income"""
        self.assertEqual(self.tracker.get_monthly_budget("2025-01"), 0.0)
    
    def test_get_yearly_budget_nonexistent(self):
        """Test getting budget for a year with no income"""
        self.assertEqual(self.tracker.get_yearly_budget("2025"), 0.0)
    
    def test_get_all_daily_budgets(self):
        """Test getting all daily budgets"""
        self.tracker.add_daily_income(100.0, "2025-01-15")
        self.tracker.add_daily_income(200.0, "2025-01-16")
        budgets = self.tracker.get_all_daily_budgets()
        self.assertEqual(len(budgets), 2)
        self.assertEqual(budgets["2025-01-15"], 100.0)
        self.assertEqual(budgets["2025-01-16"], 200.0)
    
    def test_get_all_monthly_budgets(self):
        """Test getting all monthly budgets"""
        self.tracker.add_monthly_income(3000.0, "2025-01")
        self.tracker.add_monthly_income(3500.0, "2025-02")
        budgets = self.tracker.get_all_monthly_budgets()
        self.assertEqual(len(budgets), 2)
        self.assertEqual(budgets["2025-01"], 3000.0)
        self.assertEqual(budgets["2025-02"], 3500.0)
    
    def test_get_all_yearly_budgets(self):
        """Test getting all yearly budgets"""
        self.tracker.add_yearly_income(50000.0, "2024")
        self.tracker.add_yearly_income(60000.0, "2025")
        budgets = self.tracker.get_all_yearly_budgets()
        self.assertEqual(len(budgets), 2)
        self.assertEqual(budgets["2024"], 50000.0)
        self.assertEqual(budgets["2025"], 60000.0)
    
    def test_save_and_load_file(self):
        """Test saving and loading budget data"""
        self.tracker.add_daily_income(100.0, "2025-01-15")
        self.tracker.add_monthly_income(3000.0, "2025-01")
        self.tracker.add_yearly_income(50000.0, "2025")
        
        self.tracker.save_to_file(self.test_file)
        
        new_tracker = BudgetTracker()
        new_tracker.load_from_file(self.test_file)
        
        self.assertEqual(new_tracker.get_daily_budget("2025-01-15"), 100.0)
        self.assertEqual(new_tracker.get_monthly_budget("2025-01"), 3000.0)
        self.assertEqual(new_tracker.get_yearly_budget("2025"), 50000.0)
    
    def test_load_nonexistent_file(self):
        """Test loading from a nonexistent file"""
        # Should not raise an error, just leave tracker empty
        self.tracker.load_from_file("nonexistent_file.json")
        self.assertEqual(len(self.tracker.get_all_daily_budgets()), 0)
    
    def test_get_summary(self):
        """Test getting budget summary"""
        self.tracker.add_daily_income(100.0, "2025-01-15")
        self.tracker.add_monthly_income(3000.0, "2025-01")
        self.tracker.add_yearly_income(50000.0, "2025")
        
        summary = self.tracker.get_summary()
        self.assertIn("Budget Summary", summary)
        self.assertIn("2025-01-15", summary)
        self.assertIn("100.00", summary)
        self.assertIn("2025-01", summary)
        self.assertIn("3000.00", summary)
        self.assertIn("2025", summary)
        self.assertIn("50000.00", summary)
    
    def test_empty_summary(self):
        """Test getting summary with no budgets"""
        summary = self.tracker.get_summary()
        self.assertIn("No daily budgets recorded", summary)
        self.assertIn("No monthly budgets recorded", summary)
        self.assertIn("No yearly budgets recorded", summary)


if __name__ == '__main__':
    unittest.main()
