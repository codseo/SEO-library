import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

class KeywordAnalyzer:

    def __init__(self, text):
        self.text = text
        self.stop_words = set(stopwords.words('english'))

    def _preprocess_text(self):
        text = self.text.lower()
        text = text.replace('.', ' ')
        text = text.replace(',', ' ')
        text = text.replace(';', ' ')
        text = text.replace('!', ' ')
        text = text.replace('?', ' ')
        text = text.replace('(', ' ')
        text = text.replace(')', ' ')
        text = text.replace('"', ' ')
        text = text.replace("'", ' ')
        return text

    def extract_keywords(self):
        preprocessed_text = self._preprocess_text()
        tokens = word_tokenize(preprocessed_text)
        filtered_tokens = [token for token in tokens if token not in self.stop_words]
        keywords = Counter(filtered_tokens).most_common(10)
        return keywords

    def get_keyword_density(self, keyword):
        preprocessed_text = self._preprocess_text()
        tokens = word_tokenize(preprocessed_text)
        keyword_count = 0
        for token in tokens:
            if token == keyword:
                keyword_count += 1
        return keyword_count / len(tokens)


# مثال استفاده از کتابخانه

text = "این یک متن نمونه برای تحلیل کلمات کلیدی است. در این متن سعی شده است از کلمات کلیدی مختلفی استفاده شود تا عملکرد کتابخانه به طور کامل بررسی شود."

keyword_analyzer = KeywordAnalyzer(text)

keywords = keyword_analyzer.extract_keywords()

print("کلمات کلیدی:", keywords)

keyword_density = keyword_analyzer.get_keyword_density("تحلیل")

print("چگالی کلمه کلیدی 'تحلیل':", keyword_density)

