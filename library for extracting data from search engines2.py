import requests
from bs4 import BeautifulSoup

class SearchEngineScraper:

    def __init__(self, search_engine, query):
        self.search_engine = search_engine
        self.query = query

    def get_search_results(self):
        if self.search_engine == 'google':
            url = 'https://www.google.com/search?q=' + self.query
        elif self.search_engine == 'bing':
            url = 'https://www.bing.com/search?q=' + self.query
        else:
            raise ValueError('موتور جستجوی نامعتبر')
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    def extract_titles(self):
        soup = self.get_search_results()
        titles = []
        for result in soup.find_all('h3', class_='r'):
            title = result.find('a').text
            titles.append(title)
        return titles

    def extract_descriptions(self):
        soup = self.get_search_results()
        descriptions = []
        for result in soup.find_all('div', class_='s'):
            description = result.find('span', class_='st').text
            descriptions.append(description)
        return descriptions


# مثال استفاده از کتابخانه

search_engine = 'google'
query = 'برنامه نویسی پایتون'

search_engine_scraper = SearchEngineScraper(search_engine, query)

titles = search_engine_scraper.extract_titles()

print("عنوان ها:", titles)

descriptions = search_engine_scraper.extract_descriptions()

print("توضیحات:", descriptions)
