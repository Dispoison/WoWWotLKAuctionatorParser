import cfg
import re
from data import Data


def regex(pattern, text):
    text = text.replace('\t', '').replace('\n', '')
    reg = re.compile(pattern)
    return reg.search(text)


def get_text_from_file():
    auctionator_log_path = f'{cfg.WOWPATH}\WTF\Account\{cfg.ACCOUNT_NAME.upper()}\SavedVariables\Auctionator.lua'
    server_faction = f'{cfg.SERVER_NAME}_{cfg.FACTION}'
    with open(auctionator_log_path, encoding="utf8") as fin:
        text = fin.read()
    pattern = fr'\[\"{server_faction}\"\] = \{{(?P<info>[^\}}]*)\}}'
    reg = regex(pattern, text)
    text = reg.group('info')
    return text


def text_to_data(text: str):
    splitted = text.rstrip(',').split(',')
    data = Data()
    for line in splitted:
        pattern = r'\[\"(?P<name>.*)\"\] = (?P<price>\d*)'
        reg = regex(pattern, line)
        name = reg.group('name')
        price = int(reg.group('price'))
        data.add(name, price)
    return data


def parse():
    text = get_text_from_file()
    data = text_to_data(text)
    return data
