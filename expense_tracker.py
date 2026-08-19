import json

file_name = "expenses.json"

try:
    with open(file_name, "r") as file:
        expenses = json.load(file)

except:
    expenses = []


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

        expenses.append({
            "name": name,
            "amount": amount
        })

        with open(file_name, "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expense saved! ✅")


    elif choice == "2":

        print("\nYour Expenses:")

        for expense in expenses:
            print(
                expense["name"],
                "-",
                expense["amount"]
            )


    elif choice == "3":

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total spent:", total)


    elif choice == "4":

        print("Expense Tracker closed 👋")
        break


    else:

        print("Invalid option")