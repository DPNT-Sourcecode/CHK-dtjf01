import pytest

from solutions.CHK.checkout_solution import checkout


'''
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+
'''

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
        ("a", -1),
        ("b", -1),
        ("c", -1),
        ("d", -1),
        ("E", -1),
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
        ("AAAB", 160),
        ("AAABB", 175),
        ("ABCABCA", 130 + 45 + 20 + 20),
        ("CCCDAABDDCB", 80 + 45 + 100 + 45)
    ]
)
def test_checkout(skus: str, expected: int):
    assert checkout(skus) == expected






