import keyboard
from Parser.computerworld import parse_news_titles as parse_computerworld_news
from Parser.euronews import parse_news_titles as parse_euronews_news
from Parser.cshub import parse_news_titles as parse_cshub_news
from Parser.dailywire import parse_news_titles as parse_dw_news
from Parser.grahamcluley import parse_news_titles as parse_gc_news
from Parser.thehackernews import parse_news_titles as parse_thn_news

def choose_news_channel():
    print("-------Please choose a news channel:-------")
    print("1. Computerworld")
    print("2. Cyber Security Hub (CsHub)")
    print("3. Daily Wire (dw)")
    print("4. Euronews")
    print("5. Graham Cluley - Security News")
    print("6. The Hacker News")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        parse_computerworld_news("https://www.computerworld.com/uk/")
    elif choice == "2":
        parse_cshub_news("https://www.cshub.com")
    elif choice == "3":
        parse_dw_news("https://www.dw.com/en/top-stories/s-9097")
    elif choice == "4":
        parse_euronews_news("https://www.euronews.com/")
    elif choice == "5":
        parse_gc_news("https://grahamcluley.com")
    elif choice == "6":
        parse_thn_news("https://thehackernews.com")
    else:
        print("Invalid choice!")
def main():
    print("\nWelcome to the News Retrieval System!\n")
    choose_news_channel()
    
    print("Press Esc to go back and choose another news channel or other to exit")
    state = keyboard.read_key()
    if state == "esc":
        main()

main()
