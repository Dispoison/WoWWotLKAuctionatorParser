import wow_auctionator_parser as parser
import sort

def output_prices(prices):
    with open('output.txt', 'w', encoding="utf8") as fout:
        for name, price in prices.items():
            gold = price // 10000
            silver = (price - gold * 10000) // 100
            copper = price % 100
            line_text = f'{str(name)} | {str(gold)}.{str(silver)}.{str(copper)}\n'
            fout.write(line_text)

prices = parser.parse()
glyphs = parser.only_glyphs(prices)
sorted_prices = sort.sort_prices(glyphs)

output_prices(sorted_prices)
