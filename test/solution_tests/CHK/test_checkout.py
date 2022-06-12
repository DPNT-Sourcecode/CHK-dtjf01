import pytest

from solutions.CHK.checkout_solution import (
    checkout, PRICES, OFFERS, SUBS
)


@pytest.mark.parametrize(
    "skus", ["123", 123, "a", "b", "c", "d", "aBC", "ABCd"]
)
def test_illegals(skus: str):
    assert checkout(skus) == -1


@pytest.mark.parametrize(
    "skus, value", [(k, v) for k, v in PRICES.items()]
)
def test_simple(skus: str, value: int):
    assert checkout(skus) == value




@pytest.mark.parametrize(
    "skus,expected",
    [
        (123, -1),
        ("", 0),
        ("A", 50),
        (" A", 50),
        ("A ", 50),
        ("B", 30),
        ("C", 20),
        ("D", 15),
        ("E", 40),
        ("F", 10),
        ("a", -1),
        ("b", -1),
        ("c", -1),
        ("d", -1),
        ("e", -1),
        ("f", -1),
        ("AA", 100),
        ("AB", 80),
        ("BC", 50),
        ("ABCa", -1),
        ("aABC", -1),
        ("aBcD", -1),
        ("ABCDe", -1),
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

        ("FFF", 20),
        ("FF", 20),
        ("FFFF", 30),
        ("AFFAAF", 130 + 20),
        ("AAAFFFBB", 130 + 20 + 45)
    ]
)
def test_checkout(skus: str, expected: int):
    assert checkout(skus) == expected

