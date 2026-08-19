import json


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


expenses = load_expenses()

budget = float(input("Enter your monthly budget: ₦"))


def add_expense():
    name = input("\nWhat did you spend money on? ")
    amount = float(input("How much did you spend? "))
    category = input("What category is it? ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    save_expenses()

    print("✅ Expense added:", name)


def show_expenses():
    print("\nYour expenses:")

    if not expenses:
        print("No expenses yet.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            index,
            "-",
            expense["name"],
            "₦",
            expense["amount"],
            "| Category:",
            expense["category"]
        )


def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\n💰 Total expenses:", total)


def category_totals():
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    print("\n📊 Spending by category:")

    for category, total in totals.items():
        print("-", category, "₦", total)


def budget_status():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    remaining = budget - total

    print("\n💰 Budget:", budget)
    print("💸 Total spent:", total)
    print("💵 Remaining:", remaining)


print("\n💰 Expense Tracker")

while True:

    print("\nWhat would you like to do?")

    print("1. Add expense")
    print("2. View expenses")
    print("3. Calculate total")
    print("4. Category totals")
    print("5. Budget status")
    print("6. Quit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        calculate_total()

    elif choice == "4":
        category_totals()

    elif choice == "5":
        budget_status()

    elif choice == "6":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid option. Please choose 1-6.")