import requests
from bs4 import BeautifulSoup
import webbrowser
from urllib.parse import urljoin

def parse_news_titles(url):
    print("-------Recent News-------")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    news_titles = soup.select("h3")
    recent_titles = news_titles[:5]

    for idx, title in enumerate(recent_titles, start=1):
        title_text = title.text.strip()
        print(f"{idx}. {title_text}")

    choice = input("Select the title you want to see (1-5): ")
    choice = int(choice)

    if 1 <= choice <= len(recent_titles):
        selected_title = recent_titles[choice - 1]
        link = selected_title.a["href"]
        absolute_url = urljoin(url, link)
        print("Opening in browser:", selected_title.text.strip())
        webbrowser.open(absolute_url)
    else:
        print("Invalid choice!")

#parse_news_titles("https://www.euronews.com/")
