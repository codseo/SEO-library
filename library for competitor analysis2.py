import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

class CompetitorAnalyzer:

    def __init__(self, url):
        self.url = url

    def get_website_info(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').text
        meta_description = soup.find('meta', attrs={'name': 'description'})
        if meta_description:
            meta_description = meta_description['content']
        else:
            meta_description = ''
        return title, meta_description

    def get_keywords(self):
        title, meta_description = self.get_website_info()
        text = title + ' ' + meta_description
        preprocessed_text = text.lower()
        preprocessed_text = text.replace('.', ' ')
        preprocessed_text = text.replace(',', ' ')
        preprocessed_text = text.replace(';', ' ')
        preprocessed_text = text.replace('!', ' ')
        preprocessed_text = text.replace('?', ' ')
        preprocessed_text = text.replace('(', ' ')
        preprocessed_text = text.replace(')', ' ')
        preprocessed_text = text.replace('"', ' ')
        preprocessed_text = text.replace("'", ' ')
        tokens = word_tokenize(preprocessed_text)
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token for token in tokens if token not in stop_words]
        keywords = Counter(filtered_tokens).most_common(10)
        return keywords

    def get_backlinks(self):
        # برای استفاده از این تابع باید API Key خود را از سایت Moz دریافت کنید
        api_key = 'YOUR_API_KEY'
        headers = {'Authorization': 'Bearer ' + api_key}
        response = requests.get('https://api.moz.com/v1/domains/links?url=' + self.url, headers=headers)
        data = response.json()
        return data['links']


# مثال استفاده از کتابخانه

url = "https://www.example.com"

competitor_analyzer = CompetitorAnalyzer(url)

title, meta_description = competitor_analyzer.get_website_info()

print("عنوان:", title)
print("توضیحات متا:", meta_description)

keywords = competitor_analyzer.get_keywords()

print("کلمات کلیدی:", keywords)

backlinks = competitor_analyzer.get_backlinks()

print("تعداد بک لینک ها:", len(backlinks))
