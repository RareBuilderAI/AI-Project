import requests

print("News Aggregator 📰")

topic = input("Enter news topic: ")

api_key = "1eb7b572fc0d462ea7315e8b2563c391"

url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"

response = requests.get(url)

data = response.json()

if data["status"] == "ok":

    articles = data["articles"]

    print("\nTop News Headlines 📰")

    for index, article in enumerate(articles[:5], start=1):
        print("\n", index, article["title"])

else:
    print("Error:", data["message"])