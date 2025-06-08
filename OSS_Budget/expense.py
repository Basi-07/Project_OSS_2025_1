
class Expense:
    def __init__(self, date, category, description, amount, tags=None):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
        self.tags = tags or [] 

    def __str__(self):
        tag_str = ", ".join(self.tags) if self.tags else "-"
        return f"[{self.date}] {self.category} - {self.description}: {self.amount}원 | 태그: {tag_str}"
