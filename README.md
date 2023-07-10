# Cyber Security News Scraper

The main purpose of this script is facilitate the access to quality, relevant and most recent cyber security news articles/events by scraping and automating the news retrieval from specific news channels.

## Deployment

To run this script, one can use the following:

```bash
python csnews.py
```

It could also be deployed using python3 depending on the installed version.

## Dependencies

This project relies on the following libraries:

`requests` (version x.x.x): Used for making HTTP requests to retrieve web content.
`beautifulsoup4` (version x.x.x): Used for parsing HTML and extracting information from web pages.
`webbrowser` (standard library): Used for opening URLs in a web browser.
`urllib.parse` (standard library): Used for parsing and manipulating URLs.
`keyboard` (version x.x.x): Used for capturing keyboard events for user input.
You can install these dependencies using pip. Run the following command to install them:

`pip install ("library name goes here")`
Please ensure that you have pip installed before running the command.

Note: The webbrowser and urllib.parse libraries are standard libraries in Python and do not require separate installation

## Features
Feature 1: Provide a list of recent news articles from various sources.
Feature 2: Allow users to choose a news channel and view the latest headlines.
Feature 3: Open selected news articles in a web browser for more details.
Feature 4: Handle user input and provide a menu for navigation and interaction.
Feature 5: Support for multiple news channels and websites.
Feature 6: User-friendly interface with keyboard controls.
Feature 7: Error handling for invalid user input and network connectivity issues.

## FAQ

### Q1: How do I choose a news channel?
A: When you run the program, you will be presented with a menu of news channels. Simply enter the corresponding number of the desired news channel and press Enter.

### Q2: Can I add more news channels?
A: Yes, you can easily add more news channels by extending the code in the `choose_news_channel()` function. Simply follow the existing pattern and add an option for the new news channel along with its corresponding function import and parsing logic. Please do understand that different websites may represent different types of code or approaches on how to be scrapped. When attempting to add another news channel it is important to analyze its website's html stucture as a way to scrape the correct elements.

### Q3: How do I navigate between articles?
A: After selecting a news article, you can open it in a web browser for more details. Once you are done reading the article, you can press 'E' to exit or simply interrupt the execution of the file with the `Ctrl+C command`.

### Q4: How can I contribute to this project?
A: Contributions are welcome! If you would like to contribute to the project, please follow the standard GitHub workflow. Fork the repository, make your changes, and submit a pull request. Be sure to provide a clear description of the changes you have made.

### Q5: How can I report a bug or suggest an improvement?
A: If you encounter any bugs or have suggestions for improvements, please open an issue on the project's GitHub repository. Provide detailed information about the problem or suggestion, and it will be addressed as soon as possible.

### Q6: Are there any known limitations or known issues?
A: Currently, the program only retrieves the recent news titles and opens selected articles in a web browser. It does not support additional functionalities such as searching, filtering, or bookmarking. As for issues, the only that can possibly be mentioned is the functionality of the code be fully dependent on the HTML strucure of the websites being scraped. That implies that if the HTML structure changes the code would present errors.