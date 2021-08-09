class Data:
    def __init__(self, records=dict()):
        self.records = records

    def __getitem__(self, item):
        if isinstance(item, int):
            name = list(self.records)[0]
            price = list(self.records.values())[0]
            return Data({name: price})
        return Data({k: self.records[k] for k in list(self.records)[item]})

    def add(self, key, value):
        self.records[key] = value

    def filter(self, condition, *texts):
        filtered_records = dict()
        for text in texts:
            filtered_records |= {name: price for name, price in self.records.items() if condition(name, text)}
        return Data(filtered_records)

    def startswith(self, *texts):
        return self.filter(lambda name, text: name.lower().startswith(text.lower()), *texts)

    def endswith(self, *texts):
        return self.filter(lambda name, text: name.lower().endswith(text.lower()), *texts)

    def search(self, *texts):
        return self.filter(lambda name, text: text.lower() in name.lower(), *texts)

    def sort(self, reverse=True):
        return Data({name: price for name, price in sorted(self.records.items(), key=lambda p: p[1], reverse=reverse)})
