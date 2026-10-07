import requests, pandas as pd
from bs4 import BeautifulSoup

books = []
for page in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    for b in soup.select("article.product_pod"):
        books.append({
            "title": b.h3.a["title"],
            "price": b.select_one(".price_color").text,
            "rating": b.p["class"][1],
        })

df = pd.DataFrame(books)
print(df.info())
df.to_csv("books.csv", index=False)
print("Scraping completed. Data saved to books.csv")
