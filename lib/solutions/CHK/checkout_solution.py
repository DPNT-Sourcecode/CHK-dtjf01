
PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}

OFFERS = {
    "AAA": 130,
    "BB": 45
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # sort the string into groups of SKUs
    s_skus = sorted(skus.upper())
    # combine offers of SKUs

    # calc price
    total = sum([PRICES.get(s, 0) for s in s_skus])
    # return sum of SKU groups
    return total



