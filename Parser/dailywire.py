import requests
from bs4 import BeautifulSoup
import webbrowser
from urllib.parse import urljoin

def parse_news_titles(url):
    base_url = "https://www.dw.com/en/top-stories/s-9097"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, "html.parser")
    news_titles = soup.select("h3 a")
    recent_titles = news_titles[:5]

    print("-------Recent News-------")
    for i, title in enumerate(recent_titles, start=1):
        print(f"{i}. {title.text.strip()}")

    choice = input("Select the title you want to see (1-5): ")
    try:
        choice = int(choice)
        if 1 <= choice <= 5:
            selected_title = news_titles[choice - 1]
            article_url = selected_title["href"]
            full_url = urljoin(base_url, article_url)
            webbrowser.open(full_url)
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid choice. Please enter a valid number.")

#if __name__ == "__main__":
    #parse_news_titles()
