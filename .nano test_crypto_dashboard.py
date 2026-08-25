from crypto_dashboard import CryptoDashboard


dashboard = CryptoDashboard()


print(
    dashboard.add_crypto(
        "Bitcoin",
        0.5,
        60000
    )
)


print(
    dashboard.add_crypto(
        "Ethereum",
        2,
        3000
    )
)


print(
    dashboard.show_portfolio()
)

