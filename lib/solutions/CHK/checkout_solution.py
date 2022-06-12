
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
    # if any invalue value -> return -1
    if any([s not in PRICES for s in s_skus]):
        return -1

    # combine offers of SKUs

    # calc price
    total = sum([PRICES[s] for s in s_skus])
    # return sum of SKU groups
    return total





