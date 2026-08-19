import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TEST_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(
    "https://httpbin.org/anything",
    headers=headers
)

print("Status:", response.status_code)