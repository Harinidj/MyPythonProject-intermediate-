class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.savings = 0

    def set_income(self, amount):
        self.income = amount

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def calculate_savings(self):
        self.savings = self.income - sum(self.expenses.values())

    def display_budget(self):
        print("Income: $", self.income)
        print("Expenses:")
        for category, amount in self.expenses.items():
            print(category, ": Rs", amount)
        print("Savings: Rs", self.savings)

    def get_saving_ideas(self):
        if self.savings < 0:
            return "You're in debt! Consider reducing expenses or increasing income."
        elif self.savings < self.income * 0.1:
            return "Try to save at least 10% of your income. Consider cutting back on unnecessary expenses."
        elif self.savings < self.income * 0.2:
            return "You're on the right track! Consider increasing your savings rate or investing in a retirement account."
        else:
            return "Great job! You're saving a significant portion of your income. Consider exploring other investment options or charitable giving."

def main():
    tracker = BudgetTracker()

    print("Welcome to the budget tracker!")
    income = float(input("Enter your monthly income: Rs"))
    tracker.set_income(income)

    while True:
        print("\nOptions:")
        print("1. Add expense")
        print("2. Calculate savings")
        print("3. Display budget")
        print("4. Get saving ideas")
        print("5. Quit")

        option = input("Choose an option: ")

        if option == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: Rs"))
            tracker.add_expense(category, amount)
        elif option == "2":
            tracker.calculate_savings()
        elif option == "3":
            tracker.display_budget()
        elif option == "4":
            print(tracker.get_saving_ideas())
        elif option == "5":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
