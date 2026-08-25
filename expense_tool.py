import json


class ExpenseTool:

    def __init__(self):

        self.file = "expenses.json"


    def load_expenses(self):

        try:

            with open(self.file, "r") as f:

                return json.load(f)

        except FileNotFoundError:

            return []


    def save_expenses(self, expenses):

        with open(self.file, "w") as f:

            json.dump(expenses, f, indent=4)


    def add_expense(self, name, amount):

        expenses = self.load_expenses()


        expenses.append(
            {
                "name": name,
                "amount": amount
            }
        )


        self.save_expenses(expenses)


        return "💰 Expense added successfully!"


    def view_expenses(self):

        expenses = self.load_expenses()


        if not expenses:

            return "No expenses found."


        result = "💰 Expenses:\n\n"

        total = 0


        for index, expense in enumerate(expenses, 1):

            result += (
                f"{index}. "
                f"{expense['name']}: "
                f"${expense['amount']}\n"
            )

            total += expense["amount"]


        result += f"\nTotal: ${total}"


        return result
