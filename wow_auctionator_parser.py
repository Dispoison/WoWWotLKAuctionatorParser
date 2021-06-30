import cfg
import re


def regex(pattern, text):
    text = text.replace('\t', '').replace('\n', '')
    regex = re.compile(pattern)
    return regex.search(text)


def to_dict(text: str):
    splited = text.rstrip(',').split(',')
    prices = dict()
    for line in splited:
        pattern = r'\[\"(?P<name>.*)\"\] = (?P<price>\d*)'
        reg = regex(pattern, line)
        name = reg.group('name')
        price = reg.group('price')
        prices[name] = int(price)
    return prices


def parse():
    auctionator_log_path = f'{cfg.WOWPATH}\WTF\Account\{cfg.ACCOUNT_NAME.upper()}\SavedVariables\Auctionator.lua'
    server_faction = f'{cfg.SERVER_NAME}_{cfg.FACTION}'
    with open(auctionator_log_path, encoding="utf8") as fin:
        text = fin.read()
    pattern = fr'\[\"{server_faction}\"\] = \{{(?P<info>[^\}}]*)\}}'
    reg = regex(pattern, text)
    info = reg.group('info')
    return to_dict(info)


def only_glyphs(prices):
    return {name: price for name, price in prices.items() if name.startswith('Символ')}
