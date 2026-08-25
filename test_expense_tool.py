from expense_tool import ExpenseTool


expense = ExpenseTool()


print(
    expense.add_expense(
        "Food",
        20
    )
)


print(
    expense.add_expense(
        "Transport",
        10
    )
)


print(
    expense.view_expenses()
)
