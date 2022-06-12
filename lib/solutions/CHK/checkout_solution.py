
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
    # if not a string -> -1
    if not isinstance(skus, str):
        return -1

    # sort the string into groups of SKUs
    s_skus = "".join(sorted(skus.strip()))

    if not skus:
        return -1

    # if any invalid value -> return -1
    if any([s not in PRICES for s in s_skus]):
        return -1

    total = 0
    for k, v in OFFERS.items():
        total += s_skus.count(k) * v
        s_skus = s_skus.replace(k, "")

    # calc price of remaining
    total += sum([PRICES[s] for s in s_skus])
    # return sum of SKU groups
    return total




