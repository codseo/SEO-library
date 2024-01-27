import requests
from bs4 import BeautifulSoup

class SearchEngineDataExtractor:

    def __init__(self, query):
        self.query = query

    def get_google_results(self):
        url = 'https://www.google.com/search?q=' + self.query
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        results = []
        for result in soup.find_all('div', class_='result'):
            title = result.find('h3').text
            link = result.find('a')['href']
            description = result.find('p').text
            results.append((title, link, description))
        return results

    def get_bing_results(self):
        url = 'https://www.bing.com/search?q=' + self.query
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        results = []
        for result in soup.find_all('div', class_='b_algo'):
            title = result.find('h2').text
            link = result.find('a')['href']
            description = result.find('p').text
            results.append((title, link, description))
        return results


# مثال استفاده از کتابخانه

query = "برنامه نویسی پایتون"

search_engine_data_extractor = SearchEngineDataExtractor(query)

google_results = search_engine_data_extractor.get_google_results()

print("نتایج گوگل:", google_results)

bing_results = search_engine_data_extractor.get_bing_results()

print("نتایج بینگ:", bing_results)
