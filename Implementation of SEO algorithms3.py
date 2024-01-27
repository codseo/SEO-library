import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

class SEOAlgorithm:

    def __init__(self, url):
        self.url = url

    def get_keyword_density(self, keyword):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(text)
        filtered_tokens = [token for token in tokens if token not in stop_words]
        keyword_count = 0
        for token in filtered_tokens:
            if token == keyword:
                keyword_count += 1
        return keyword_count / len(filtered_tokens)

    def get_title_tag(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.text
        return title

    def get_meta_description(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        description = soup.find('meta', {'name': 'description'})['content']
        return description

    def get_backlinks(self):
        # برای استفاده از این تابع باید API Key خود را از سایت Moz دریافت کنید
        api_key = 'YOUR_API_KEY'
        headers = {'Authorization': 'Bearer ' + api_key}
        response = requests.get('https://api.moz.com/v1/domains/links?url=' + self.url, headers=headers)
        data = response.json()
        return data['links']


# مثال استفاده از کتابخانه

url = "https://www.example.com"

seo_algorithm = SEOAlgorithm(url)

keyword_density = seo_algorithm.get_keyword_density("برنامه نویسی پایتون")

print("چگالی کلمه کلیدی 'برنامه نویسی پایتون':", keyword_density)

title_tag = seo_algorithm.get_title_tag()

print("عنوان:", title_tag)

meta_description = seo_algorithm.get_meta_description()

print("توضیحات متا:", meta_description)

backlinks = seo_algorithm.get_backlinks()

print("تعداد بک لینک ها:", len(backlinks))
