import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount, tags=None):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount, tags)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def tag_spending_ratio(self, tag):
        total = sum(e.amount for e in self.expenses)
        if total == 0:
            print("지출 내역이 없습니다.\n")
            return

        tag_total = sum(e.amount for e in self.expenses if tag in e.tags)
        ratio = (tag_total / total) * 100
        print(f"태그 '{tag}' 관련 지출: {tag_total}원 (전체의 {ratio:.2f}%)\n")
