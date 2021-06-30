def convert_money(money):
    """Convert money value to gold, silver and copper"""
    gold = money // 10000
    silver = (money - gold * 10000) // 100
    copper = money % 100
    return gold, silver, copper


def output_prices(prices):
    """Create or rewrite 'output.txt' file with needed information"""
    line_text = ''
    for name, price in prices.items():
        gold, silver, copper = convert_money(price)
        line_text += f'{str(name)} | {str(gold)}.{str(silver)}.{str(copper)}\n'

    with open('output.txt', 'w', encoding="utf8") as fout:
        fout.write(line_text)


def display_prices(prices):
    """Print needed information in console"""
    for name, price in prices.items():
        gold, silver, copper = convert_money(price)
        line_text = f'{str(name)} | {str(gold)}.{str(silver)}.{str(copper)}'
        print(line_text)
