import requests
from bs4 import BeautifulSoup
import csv

url="https://books.toscrape.com/"

response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")


book=[]

for item in soup.find_all("article",class_="product_pod"):
    title=item.h3.a['title']
    price=item.find("p",class_="price_color").get_text(strip=True)
    availability=item.find("p",class_="instock availability").get_text(strip=True)
    book.append([title,price,availability])

with open("book_parsed.csv","w",newline="",encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerow(["Title","Price","Availability"])
    writer.writerows(book)

print(f"Saved {len(book)} Product Details\n")
