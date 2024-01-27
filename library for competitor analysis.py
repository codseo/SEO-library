import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

class CompetitorAnalyzer:

    def __init__(self, competitor_url):
        self.competitor_url = competitor_url

    def get_website_info(self):
        response = requests.get(self.competitor_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').text
        meta_description = soup.find('meta', {'name': 'description'})['content']
        return title, meta_description

    def get_top_keywords(self):
        response = requests.get(self.competitor_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(text)
        filtered_tokens = [token for token in tokens if token not in stop_words]
        keywords = Counter(filtered_tokens).most_common(10)
        return keywords

    def get_backlinks(self):
        # برای استفاده از این تابع باید API Key خود را از سایت Moz دریافت کنید
        api_key = 'YOUR_API_KEY'
        headers = {'Authorization': 'Bearer ' + api_key}
        response = requests.get('https://api.moz.com/v1/domains/links?url=' + self.competitor_url, headers=headers)
        data = response.json()
        return data['links']


# مثال استفاده از کتابخانه

competitor_url = "https://www.example.com"

competitor_analyzer = CompetitorAnalyzer(competitor_url)

title, meta_description = competitor_analyzer.get_website_info()

print("عنوان وب سایت:", title)
print("توضیحات متا:", meta_description)

keywords = competitor_analyzer.get_top_keywords()

print("کلمات کلیدی برتر:", keywords)

backlinks = competitor_analyzer.get_backlinks()

print("تعداد بک لینک ها:", len(backlinks))
