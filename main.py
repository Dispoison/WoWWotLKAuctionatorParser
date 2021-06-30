from auctionator_parser import parse
from output import display_prices, output_prices

data = parse().startswith('Символ').sort().top(5)

display_prices(data)
