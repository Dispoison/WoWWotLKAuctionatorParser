from auctionator_parser import parse
from output import display, output

data = parse()


def glyphs():
    glyphs_ = data.search('Символ').sort()[:25]
    output(glyphs_, 'glyphs.txt')


def sockets_main():
    sockets = data.search('багровый рубин', 'царский янтарь', 'Величественный циркон').sort()
    display(sockets)


def sockets_all():
    sockets = data.search('багровый рубин', 'царский янтарь', 'Величественный циркон',
                          'Аметрин', 'Око Зула', 'Страхолит').sort()
    display(sockets)


glyphs()
