# News Headlines Scraper

**This Python script retrieves and displays the latest news headlines from a specified URL using web scraping techniques. It utilizes the requests library to fetch the HTML content and BeautifulSoup for parsing and extracting relevant information.**

**Usage**
Ensure you have Python installed on your machine.
Install the required libraries by running:
pip install requests
pip install beautifulsoup4
Run the script using:
python script_name.py

Description
The script is designed to fetch news headlines from the BBC News website (https://www.bbc.com/news) as an example. You can customize the news_url variable in the script to point to a different news website.
The extracted information includes the article title, source, and link. The script prints the details for each headline found on the specified website.

**Dependencies**
requests - HTTP library for making requests.
BeautifulSoup - Library for pulling data out of HTML and XML files.

**Installation**
You can install the required libraries using the following commands:

pip install requests
pip install beautifulsoup4

**Execution**
Run the script by executing:
python script_name.py

**Notes**
If the script fails to retrieve news, it will print the HTTP status code.
If no headlines are found on the website, a corresponding message will be displayed.
