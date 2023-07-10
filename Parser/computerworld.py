import requests
from bs4 import BeautifulSoup
import webbrowser
from urllib.parse import urljoin

def parse_news_titles(url):
    print("-------Recent News-------")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    news_titles = soup.select("#homepage .homepage-crawl h3")
    recent_titles = news_titles[:5]

    for idx, title in enumerate(recent_titles, start=1):
        title_text = title.text.strip()
        title_link = urljoin(url, title.find("a")["href"])
        print(f"{idx}. {title_text}")

    choice = input("Select the title you want to see (1-5): ")
    choice = int(choice)

    if 1 <= choice <= len(recent_titles):
        selected_title = recent_titles[choice - 1]
        title_link = urljoin(url, selected_title.find("a")["href"])
        print("Opening in browser:", selected_title.text.strip())
        webbrowser.open(title_link)
    else:
        print("Invalid choice!")

# parse_news_titles("https://www.computerworld.com/uk/")
