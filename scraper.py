import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Starting scraper...")

url = "https://quotes.toscrape.com/"
response = requests.get(url)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []

for quote in soup.find_all("span", class_="text"):
    quotes.append(quote.text)

print("Quotes found:", len(quotes))

df = pd.DataFrame(quotes, columns=["Quotes"])
df.to_csv("headlines.csv", index=False)

print("Data saved successfully!")