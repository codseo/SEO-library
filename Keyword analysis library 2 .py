import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class KeywordAnalyzer:

    def __init__(self, text):
        self.text = text
        self.stop_words = set(stopwords.words('english'))

    def extract_keywords(self):
        # تبدیل متن به حروف کوچک
        text = self.text.lower()

        # توکنیزه کردن متن
        tokens = word_tokenize(text)

        # حذف کلمات توقف
        keywords = [token for token in tokens if token not in self.stop_words]

        # حذف علائم نگارشی
        keywords = [token for token in keywords if token.isalpha()]

        # برگرداندن کلمات کلیدی
        return keywords

    def get_keyword_frequencies(self):
        keywords = self.extract_keywords()
        frequencies = {}
        for keyword in keywords:
            if keyword in frequencies:
                frequencies[keyword] += 1
            else:
                frequencies[keyword] = 1
        return frequencies

    def get_most_frequent_keywords(self, n=10):
        frequencies = self.get_keyword_frequencies()
        most_frequent_keywords = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)[:n]
        return [keyword for keyword, frequency in most_frequent_keywords]


# مثال استفاده

text = """
این یک متن نمونه برای تحلیل کلمات کلیدی است. 
در این متن سعی شده است از کلمات کلیدی مختلف 
در حوزه های مختلف استفاده شود.
"""

keyword_analyzer = KeywordAnalyzer(text)

# استخراج کلمات کلیدی
keywords = keyword_analyzer.extract_keywords()
print(keywords)

# دریافت فراوانی کلمات کلیدی
frequencies = keyword_analyzer.get_keyword_frequencies()
print(frequencies)

# دریافت n کلمه کلیدی با بیشترین فراوانی
most_frequent_keywords = keyword_analyzer.get_most_frequent_keywords(n=5)
print(most_frequent_keywords)
