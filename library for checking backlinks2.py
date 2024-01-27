import requests
from bs4 import BeautifulSoup

class BacklinkChecker:

    def __init__(self, url):
        self.url = url

    def get_backlinks(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')
        backlinks = []
        for link in links:
            href = link.get('href')
            if href and href.startswith('http'):
                backlinks.append(href)
        return backlinks

    def get_domain_authority(self):
        # برای استفاده از این تابع باید API Key خود را از سایت Moz دریافت کنید
        api_key = 'YOUR_API_KEY'
        headers = {'Authorization': 'Bearer ' + api_key}
        response = requests.get('https://api.moz.com/v1/domains/links?url=' + self.url, headers=headers)
        data = response.json()
        return data['domain_authority']


# مثال استفاده از کتابخانه

url = "https://www.example.com"

backlink_checker = BacklinkChecker(url)

backlinks = backlink_checker.get_backlinks()

print("تعداد بک لینک ها:", len(backlinks))

domain_authority = backlink_checker.get_domain_authority()

print("Domain Authority:", domain_authority)
