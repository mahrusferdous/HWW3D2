class BudgetCategory:

    def __init__(self, name, budget, expenses=0):
        self.__name = name
        self.__budget = budget
        self.__expenses = expenses

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_budget(self):
        return self.__budget

    def set_budget(self, budget):
        if budget > 0:
            self.__budget = budget
        else:
            print("Budget must be positive")

    def get_expenses(self):
        return self.__expenses

    def set_expenses(self, expenses):
        if expenses > 0 and self.get_budget() > expenses:
            self.__expenses = expenses
            self.set_budget(self.get_budget() - expenses)
        else:
            print("You have exceeded the limit")

    def budget_details(self):
        print(
            f"Your total budget for {self.get_name()} was {self.get_budget() + self.get_expenses()} and after your {self.get_expenses()} expenses your budget deducted to {self.get_budget()}"
        )


budget = BudgetCategory("Food", 1000)
print(budget.get_budget())
budget.set_budget(2000)
print(budget.get_budget())

print(budget.get_name())
budget.set_name("Movies")
print(budget.get_name())

budget.set_expenses(199)
print(budget.get_expenses())

print()
budget.budget_details()
