import requests
from bs4 import BeautifulSoup
import webbrowser

def parse_news_titles(url):
    print("-------Recent News-------")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    parent_elements = soup.select("div.body-post.clear")  
    
    recent_titles = []
    for parent_element in parent_elements:
        title_element = parent_element.select_one("h2")  
        if title_element:
            title = title_element.text.strip()
            recent_titles.append(title)

    for idx, title in enumerate(recent_titles, start=1):
        print(f"{idx}. {title}")

    choice = input("Select the title you want to see (1-9): ")
    choice = int(choice)

    if 1 <= choice <= len(recent_titles):
        selected_title = recent_titles[choice - 1]
        link_element = parent_elements[choice - 1].select_one("a.story-link")  
        if link_element:
            link = link_element["href"]
            print("Opening in browser:", selected_title)
            webbrowser.open(link)
        else:
            print("Link not found")
    else:
        print("Invalid choice!")

#parse_news_titles("https://thehackernews.com")