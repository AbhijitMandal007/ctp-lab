import requests
from bs4 import BeautifulSoup


url="https://news.ycombinator.com/"

def fetch_headline(url):
    response=requests.get(url)
    response.raise_for_status()

    soup=BeautifulSoup(response.text,"html.parser")
    headlines=[]

    for span in soup.find_all("span",class_="titleline"):
        link_tag=span.find("a")
        if(link_tag):
            title=link_tag.get_text(strip=True)
            link=link_tag.get("href")
            headlines.append((title,link))

    return headlines


headlines=fetch_headline(url)

print(f"Parsed {len(headlines)} Headlines\n")

for i, (title,link) in enumerate(headlines,start=1):
    print(f"{i}, {title}")
    print(f" {link}\n")

print("Parsing a news website completed successfully")
    



