def sort_prices(prices):
    return {k: v for k, v in sorted(prices.items(), key=lambda item: item[1], reverse=True)}
