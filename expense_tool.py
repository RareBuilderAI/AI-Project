import json


class ExpenseTool:

    def __init__(self):

        self.file = "expenses.json"


    def load_expenses(self):

        try:

            with open(self.file, "r") as f:

                return json.load(f)

        except (FileNotFoundError, json.JSONDecodeError):

            return []


    def save_expenses(self, expenses):

        with open(self.file, "w") as f:

            json.dump(
                expenses,
                f,
                indent=4
            )


    def add_expense(self, name, amount):

        expenses = self.load_expenses()

        expenses.append(
            {
                "name": name,
                "amount": float(amount)
            }
        )

        self.save_expenses(expenses)

        return "💰 Expense added successfully!"


    def view_expenses(self):

        expenses = self.load_expenses()

        if not expenses:

            return "💰 No expenses found."


        result = "💰 Expenses:\n\n"

        total = 0


        for index, expense in enumerate(expenses, 1):

            amount = float(expense["amount"])

            total += amount

            result += (
                f"{index}. "
                f"{expense['name']} — "
                f"₦{amount:,.2f}\n"
            )


        result += (
            f"\nTotal: ₦{total:,.2f}"
        )

        return result


    def delete_expense(self, expense_number):

        expenses = self.load_expenses()

        try:

            index = int(expense_number) - 1

        except ValueError:

            return "Please provide a valid expense number."


        if index < 0 or index >= len(expenses):

            return "That expense does not exist."


        deleted_expense = expenses.pop(index)

        self.save_expenses(expenses)

        return (
            f"🗑️ Expense deleted: "
            f"{deleted_expense['name']}"
        )
