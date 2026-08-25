from crypto_tool import CryptoTool


crypto = CryptoTool()


print(
    crypto.add_crypto(
        "Bitcoin",
        2,
        75000
    )
)


print(
    crypto.show_portfolio()
)
