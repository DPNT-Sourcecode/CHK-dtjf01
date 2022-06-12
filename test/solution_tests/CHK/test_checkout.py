import pytest
import itertools

import random

from solutions.CHK.checkout_solution import (
    COMBO_OFFERS, checkout, PRICES
)


COMBOS = [
    ("AA", 100),
    ("AB", 80),
    ("BC", 50),
    ("BB", 45),
    ("ABB", 95),
    ("AAA", 130),
    ("AAAAA", 200),
    ("AAAAAA", 250),
    ("AAAB", 160),
    ("AAABB", 175),
    ("AAABBAA", 245),
    ("AABBAAB", 130 + 50 + 45 + 30),
    ("AABBAAAB", 200 + 45 + 30),
    ("ABCABCA", 130 + 45 + 20 + 20),
    ("CCCDAABDDCB", 80 + 45 + 100 + 45),
    ("EEB", 80),
    ("ABCDEE", 50 + 0 + 20 + 15 + 80),
    ("BBEE", 30 + 80),
    ("AAAAABBEE", 200 + 30 + 80),
    ("ABBEEBB", 50 + 30 + 80 + 45),
    ("BBEEBBEE", 160 + 45),

    ("FFFF", 30),
    ("AFFAAF", 130 + 20),
    ("AAAFFFBB", 130 + 20 + 45),

    ("H"*15, 125),
    ("P"*5 + "H"*5, 200 + 45),
    ("RRRQQQ", 150 + 60),


    ("AAASTX", 130 + 45),
    ("STBBZ", 45 + 45),
    ("YYY", 45),
    ("USUXUTUZ", 120 + 45 + 50)
]

GROUP_OFFERS = [
    ("".join(combo), 45)
    for combo in COMBO_OFFERS
]


@pytest.mark.parametrize(
    "skus", ["123", 123, "a", "b", "c", "d", "aBC", "ABCd", "ABCa", 
             "aABC", "aBcD", "ABCDe"]
)
def test_illegals(skus: str):
    assert checkout(skus) == -1


@pytest.mark.parametrize(
    "skus, value", [(k, v) for k, v in PRICES.items()]
)
def test_simple(skus: str, value: int):
    assert checkout(skus) == value


@pytest.mark.parametrize(
    "skus, expected",
    [
        ("AAA", 130),
        ("AAAAA", 200),
        ("BB", 45),
        ("HHHHHHHHHH", 80),
        ("HHHHH", 45),
        ("KK", 150),
        ("PPPPP", 200),
        ("QQQ", 80),
        ("VVV", 130),
        ("VV", 90)
    ]
)
def test_offers(skus: str, expected: int):
    # randomly add 'D' and scramble the input
    extra = "D" * random.randint(1, 5)
    skus = list(skus + extra)
    random.shuffle(skus)

    assert checkout("".join(skus)) == expected + PRICES[extra[0]] * len(extra)


@pytest.mark.parametrize(
    "skus, expected",
    [
        ("EEB", 80),
        ("FFF", 20),
        ("NNNM", 120),
        ("QRRR", 150),
        ("UUUU", 120),
    ]
)
def test_subs(skus: str, expected: int):
    assert checkout(skus) == expected


@pytest.mark.parametrize(
    "skus,expected", COMBOS
)
def test_combos(skus: str, expected: int):
    assert checkout(skus) == expected


@pytest.mark.parametrize(
    "skus,expected", GROUP_OFFERS
)
def test_group_offers(skus: str, expected: int):
    assert checkout(skus) == expected


@pytest.mark.parametrize(
    "skus,expected", COMBOS
)
def test_combos_shuffled(skus: str, expected: int):
    skus = list(skus)
    random.shuffle(skus)
    assert checkout("".join(skus)) == expected



