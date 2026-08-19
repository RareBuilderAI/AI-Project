import requests

print("Currency Converter 💱")

amount = float(input("Enter amount: "))

from_currency = input("From currency (example USD): ").upper()

to_currency = input("To currency (example NGN): ").upper()

url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

response = requests.get(url)

data = response.json()

if "rates" in data:

    rate = data["rates"][to_currency]

    converted = amount * rate

    print("\nConversion Result 💱")
    print(amount, from_currency, "=", converted, to_currency)

else:
    print("Currency not found ❌")