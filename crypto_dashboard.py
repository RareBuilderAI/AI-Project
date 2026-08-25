import json


class CryptoDashboard:

    def __init__(self):

        self.file_name = "crypto_portfolio.json"
        self.portfolio = self.load_portfolio()
        self.clean_duplicates()


    def load_portfolio(self):

        try:

            with open(self.file_name, "r") as file:

                return json.load(file)

        except FileNotFoundError:

            return []


    def save_portfolio(self):

        with open(self.file_name, "w") as file:

            json.dump(
                self.portfolio,
                file,
                indent=4
            )


    def clean_duplicates(self):

        cleaned = {}


        for crypto in self.portfolio:

            name = crypto["name"].lower()


            if name in cleaned:

                cleaned[name]["amount"] += crypto["amount"]

                cleaned[name]["price"] = crypto["price"]

            else:

                cleaned[name] = crypto


        self.portfolio = list(cleaned.values())

        self.save_portfolio()


    def add_crypto(self, name, amount, price):

        for crypto in self.portfolio:

            if crypto["name"].lower() == name.lower():

                crypto["amount"] = amount
                crypto["old_price"] = crypto["price"]
                crypto["price"] = price

                self.save_portfolio()

                return "♻️ Crypto updated instead of duplicated!"


        crypto = {
            "name": name,
            "amount": amount,
            "price": price,
            "old_price": price
        }


        self.portfolio.append(crypto)

        self.save_portfolio()

        return "Crypto added successfully!"


    def show_portfolio(self):

        if not self.portfolio:

            return "No crypto added yet."


        result = "₿ Crypto Portfolio:\n\n"


        for index, crypto in enumerate(self.portfolio, start=1):

            value = crypto["amount"] * crypto["price"]


            result += (
                f"{index}. {crypto['name']}\n"
                f"Amount: {crypto['amount']}\n"
                f"Price: ${crypto['price']}\n"
                f"Value: ${value}\n\n"
            )


        return result


    def price_change(self, name):

        for crypto in self.portfolio:

            if crypto["name"].lower() == name.lower():

                change = crypto["price"] - crypto["old_price"]


                if change > 0:

                    return f"📈 {name} gained ${change}"


                elif change < 0:

                    return f"📉 {name} dropped ${abs(change)}"


                else:

                    return f"➖ {name} price unchanged"


        return "Crypto not found."


    def total_value(self):

        total = 0


        for crypto in self.portfolio:

            total += crypto["amount"] * crypto["price"]


        return f"💰 Total Portfolio Value: ${total}"