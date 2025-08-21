# import dependencies
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Processor:
    def __init__(self, df):
        self.df = df

    @staticmethod
    def text_sentiment(text):
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        score = score["compound"]
        if 0.5 < score < 1:
            return "positive"
        elif -0.5 < score < 0.5:
            return "Neutral"
        elif -1 < score < -0.5:
            return "negative"
        else:
            return "Invalid value"

    @staticmethod
    def find_weapons(weapons_list, text):
        weapons_detected = ""
        text_list = text.split(" ")
        for i in text_list:
            if i in weapons_list:
                weapons_detected += i + " "
            return weapons_detected

    @staticmethod
    def rarest_word( text):
        text_list = text.split()
        sum_words = {}
        for i in text_list:
            if i not in sum_words:
                sum_words[i] = 1
            else:
                sum_words[i] += 1
        min_val = min(sum_words.values())
        for (k, v) in sum_words.items():
            if v == min_val:
                return k

    def get_text(self, row_id):
        text = self.df[self.df["_id"] == row_id][ "Text"]
        return text







