import re
from collections import Counter

class KeywordAnalyzer:

    def __init__(self, text):
        self.text = text
        self.words = self._preprocess_text(text)

    def _preprocess_text(self, text):
        # حذف علائم نگارشی
        text = re.sub(r'[^\w\s]', '', text)
        # تبدیل حروف بزرگ به حروف کوچک
        text = text.lower()
        # تبدیل متن به لیست کلمات
        words = text.split()
        return words

    def get_most_frequent_words(self, n=10):
        """
        برگرداندن n کلمه با بیشترین فرکانس
        """
        # شمارش تعداد دفعات تکرار هر کلمه
        word_counts = Counter(self.words)
        # مرتب سازی کلمات بر اساس تعداد دفعات تکرار
        most_frequent_words = word_counts.most_common(n)
        return most_frequent_words

    def get_keywords_by_tfidf(self):
        """
        برگرداندن کلمات کلیدی با استفاده از TF-IDF
        """
        # محاسبه TF برای هر کلمه
        term_frequencies = {}
        for word in self.words:
            term_frequencies[word] = self.words.count(word) / len(self.words)

        # محاسبه IDF برای هر کلمه
        document_count = 1  # در این مثال فقط یک سند داریم
        inverse_document_frequencies = {}
        for word in self.words:
            inverse_document_frequencies[word] = math.log(document_count / (1 + len([doc for doc in self.text if word in doc])))

        # محاسبه TF-IDF برای هر کلمه
        tfidf_scores = {}
        for word in self.words:
            tfidf_scores[word] = term_frequencies[word] * inverse_document_frequencies[word]

        # مرتب سازی کلمات بر اساس TF-IDF
        keywords_by_tfidf = sorted(tfidf_scores.items(), key=lambda x: x[1], reverse=True)
        return keywords_by_tfidf

# مثال استفاده از کتابخانه

text = """
این یک متن نمونه برای تحلیل کلمات کلیدی است. 
در این متن کلماتی مانند "کلمه کلیدی" و "تحلیل" 
چندین بار تکرار شده‌اند.
"""

analyzer = KeywordAnalyzer(text)

# دریافت 10 کلمه با بیشترین فرکانس
most_frequent_words = analyzer.get_most_frequent_words()
print("10 کلمه با بیشترین فرکانس:", most_frequent_words)

# دریافت کلمات کلیدی با استفاده از TF-IDF
keywords_by_tfidf = analyzer.get_keywords_by_tfidf()
print("کلمات کلیدی با استفاده از TF-IDF:", keywords_by_tfidf)
