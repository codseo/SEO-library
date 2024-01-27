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
            if href and not href.startswith('#') and not href.startswith('javascript'):
                backlinks.append(href)
        return backlinks

    def get_nofollow_backlinks(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', rel='nofollow')
        nofollow_backlinks = []
        for link in links:
            href = link.get('href')
            if href and not href.startswith('#') and not href.startswith('javascript'):
                nofollow_backlinks.append(href)
        return nofollow_backlinks


# مثال استفاده از کتابخانه

url = "https://www.example.com/"

backlink_checker = BacklinkChecker(url)

backlinks = backlink_checker.get_backlinks()

print("تعداد بک لینک ها:", len(backlinks))

nofollow_backlinks = backlink_checker.get_nofollow_backlinks()

print("تعداد بک لینک های nofollow:", len(nofollow_backlinks))
