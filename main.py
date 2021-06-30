import auctionator_parser as parser
import sort
from output import display_prices, output_prices

prices = parser.parse()
glyphs = parser.only_glyphs(prices)
sorted_prices = sort.sort_prices(glyphs)

display_prices(sorted_prices)
