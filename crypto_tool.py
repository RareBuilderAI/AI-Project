import json


class CryptoTool:

    def __init__(self):

        self.file = "crypto_portfolio.json"


    def load_portfolio(self):

        try:

            with open(self.file, "r") as f:

                return json.load(f)

        except FileNotFoundError:

            return []


    def save_portfolio(self, portfolio):

        with open(self.file, "w") as f:

            json.dump(portfolio, f, indent=4)


    def add_crypto(self, name, amount, price):

        portfolio = self.load_portfolio()


        portfolio.append(
            {
                "name": name,
                "amount": amount,
                "price": price
            }
        )


        self.save_portfolio(portfolio)


        return "₿ Crypto added successfully!"


    def show_portfolio(self):

        portfolio = self.load_portfolio()


        if not portfolio:

            return "No crypto found."


        result = "₿ Crypto Portfolio:\n\n"

        total = 0


        for index, crypto in enumerate(portfolio, 1):

            value = crypto["amount"] * crypto["price"]

            total += value


            result += (
                f"{index}. {crypto['name']}\n"
                f"Amount: {crypto['amount']}\n"
                f"Price: ${crypto['price']}\n"
                f"Value: ${value}\n\n"
            )


        result += f"💰 Total Portfolio Value: ${total}"


        return result
