import json
import os


FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []

    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(name, amount, category="general"):
    expenses = load_expenses()

    expense = {
        "name": name,
        "amount": float(amount),
        "category": category
    }

    expenses.append(expense)
    save_expenses(expenses)

    return f"Expense saved! ✅ {name} - {amount}"


def show_expenses():
    expenses = load_expenses()

    if not expenses:
        return "No expenses recorded."

    result = "💰 Your Expenses:\n\n"

    for index, expense in enumerate(expenses, start=1):
        result += (
            f"{index}. {expense['name']} - "
            f"{expense['amount']} "
            f"({expense.get('category', 'general')})\n"
        )

    return result.strip()


def calculate_total():
    expenses = load_expenses()

    total = sum(
        float(expense["amount"])
        for expense in expenses
    )

    return total


def category_totals():
    expenses = load_expenses()

    totals = {}

    for expense in expenses:
        category = expense.get("category", "general")
        amount = float(expense["amount"])

        totals[category] = totals.get(category, 0) + amount

    return totals


def budget_status(budget=None):
    total = calculate_total()

    if budget is None:
        return f"💰 Total spent: {total}"

    remaining = float(budget) - total

    return (
        f"💰 Total spent: {total}\n"
        f"📊 Budget: {budget}\n"
        f"💵 Remaining: {remaining}"
    )


def set_budget(amount):
    with open("budget.json", "w") as file:
        json.dump({"budget": float(amount)}, file, indent=4)

    return f"Budget set to {amount}"


def get_budget():
    if not os.path.exists("budget.json"):
        return None

    try:
        with open("budget.json", "r") as file:
            data = json.load(file)

        return data.get("budget")

    except (json.JSONDecodeError, OSError):
        return None


def main():
    while True:
        print("\nExpense Tracker 💰")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Expense name: ")
            amount = float(input("Amount: "))
            category = input("Category: ")

            print(
                add_expense(
                    name,
                    amount,
                    category
                )
            )

        elif choice == "2":
            print(show_expenses())

        elif choice == "3":
            print("Total spent:", calculate_total())

        elif choice == "4":
            print("Expense Tracker closed 👋")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
