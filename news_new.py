import requests
from bs4 import BeautifulSoup

def get_news_headlines(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', class_='gs-c-promo')

        if not articles:
            print(f'No headlines found on the website.')
            return

        for index, article in enumerate(articles, start=1):
            title_element = article.find('h3')
            source_element = article.find('span', class_='gs-c-source')

            title = title_element.text.strip() if title_element else 'N/A'
            source = source_element.text.strip() if source_element else 'N/A'
            link = article.find('a')['href'] if article.find('a') else 'N/A'

            print(f"{index}. {title} - {source} - {link}")

    else:
        print(f'Failed to retrieve news. Status Code: {response.status_code}')

if __name__ == "__main__":
    news_url = 'https://www.bbc.com/news'
    get_news_headlines(news_url)
