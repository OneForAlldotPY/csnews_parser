import requests
from bs4 import BeautifulSoup
import webbrowser
from urllib.parse import urljoin

def parse_news_titles(url):
    print("-------Recent News-------")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    news_titles = soup.select("#template-3 h3.article-title")
    recent_titles = news_titles[:5]

    for idx, title in enumerate(recent_titles, start=1):
        title_text = title.text.strip()
        print(f"{idx}. {title_text}")

    choice = input("Select the title you want to see (1-5): ")
    choice = int(choice)

    if 1 <= choice <= len(recent_titles):
        selected_title = recent_titles[choice - 1]
        title_link = selected_title.find("a")["href"]
        absolute_url = urljoin(url, title_link)
        print("Opening in browser:", selected_title.text.strip())
        webbrowser.open(absolute_url)
    else:
        print("Invalid choice!")

#parse_news_titles("https://www.cshub.com")

