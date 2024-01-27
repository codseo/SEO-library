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
        title = soup.title.text
        description = soup.find('meta', {'name': 'description'})['content']
        keywords = soup.find('meta', {'name': 'keywords'})['content']
        return title, description, keywords

    def get_top_keywords(self):
        response = requests.get(self.url)
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
        response = requests.get('https://api.moz.com/v1/domains/links?url=' + self.url, headers=headers)
        data = response.json()
        return data['links']


# مثال استفاده از کتابخانه

url = "https://www.example.com"

competitor_analyzer = CompetitorAnalyzer(url)

title, description, keywords = competitor_analyzer.get_website_info()

print("عنوان:", title)
print("توضیحات:", description)
print("کلمات کلیدی:", keywords)

top_keywords = competitor_analyzer.get_top_keywords()

print("کلمات کلیدی برتر:", top_keywords)

backlinks = competitor_analyzer.get_backlinks()

print("تعداد بک لینک ها:", len(backlinks))
