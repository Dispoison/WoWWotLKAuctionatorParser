from itertools import islice

class Data:
    def __init__(self):
        self.records = dict()

    def add(self, key, value):
        self.records[key] = value

    def startswith(self, text):
        self.records = {name: price for name, price in self.records.items() if name.startswith(text)}
        return self

    def top(self, number):
        self.records = {k: self.records[k] for k in list(self.records)[:number]}
        return self

    def sort(self, reverse=True):
        self.records = {k: v for k, v in sorted(self.records.items(), key=lambda item: item[1], reverse=reverse)}
        return self
