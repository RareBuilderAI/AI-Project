from customer_support_tool import CustomerSupportTool


support = CustomerSupportTool()


print(
    support.answer(
        "hello"
    )
)


print(
    support.answer(
        "I need support"
    )
)


print(
    support.answer(
        "What is your price?"
    )
)
