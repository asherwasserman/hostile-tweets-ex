import json
from processor import Processor
import pandas as pd
from fetcher import Dal

class JsonBuilder:
    def __init__(self, df:pd.DataFrame, filename):
        self.df = df
        self.filename = filename

    def get_text(self, row):
        text = row["Text"]
        return text

    def get_blacklist(self):
        with open(self.filename) as file:
            lines = [line.rstrip() for line in file]
        return lines

    def get_json(self):
        objects_list = []
        for index, row in self.df.iterrows():
            my_dict = {}
            text = self.get_text(row)
            my_dict["id"] = str(row["_id"])
            my_dict["original_text"] = text
            my_dict["rarest_word"] = Processor.rarest_word(text)
            my_dict["sentiment"] = Processor.text_sentiment(text)
            my_dict["weapons_detected"] = Processor.find_weapons(self.get_blacklist(), text)
            objects_list.append(my_dict)
        return objects_list

