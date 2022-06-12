import itertools


PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21
}

OFFERS = {
    "AAAAA": 200,
    "AAA": 130,
    "BB": 45,
    "H"*10: 80,
    "H"*5: 45,
    "KK": 150,
    "P"*5: 200,
    "QQQ": 80,
    "VVV": 130,
    "VV": 90
}

# get unique set of group permutations
COMBO_OFFERS = sorted(set(
    "".join(sorted(combo))
    for combo in itertools.combinations_with_replacement("STXYZ", 3)
))


SUBS = {
    "EE": "B",
    "FFF": "F",
    "NNN": "M",
    "RRR": "Q",
    "UUUU": "U"
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # if not a string -> -1
    if not isinstance(skus, str):
        return -1

    # sort the string into groups of SKUs
    s_skus = "".join(sorted(skus.strip()))

    # if any invalid value -> return -1
    if any([s not in PRICES for s in s_skus]):
        return -1

    # groups offers, 3 items from set -> 45
    # always favour putting expensive items in the list
    

    for k, v in SUBS.items():
        subc = s_skus.count(k)
        s_skus = s_skus.replace(v, "", subc)

    total = 0
    for k, v in OFFERS.items():
        total += s_skus.count(k) * v
        s_skus = s_skus.replace(k, "")

    # calc price of remaining
    total += sum([PRICES[s] for s in s_skus])
    # return sum of SKU groups
    return total





