from crypto_dashboard import CryptoDashboard


dashboard = CryptoDashboard()


print(
    dashboard.add_crypto(
        "Bitcoin",
        2,
        75000
    )
)


print(
    dashboard.show_portfolio()
)


print(
    dashboard.price_change(
        "Bitcoin"
    )
)


print(
    dashboard.total_value()
)