import pytest

from solutions.CHK.checkout_solution import checkout


'''
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
'''

@pytest.mark.parametrize(
    "skus,expected",
    [
        (123, -1),
        # Im assuming empty strings are illegal, not 0
        ("", -1),
        ("A", 50),
        (" A", 50),
        ("A ", 50),
        ("B", 30),
        ("C", 20),
        ("D", 15),
        ("a", 50),
        ("b", 30),
        ("c", 20),
        ("d", 15),
        ("E", -1),
        ("AA", 100),
        ("AB", 80),
        ("BC", 50),
        ("aBcD", 115),
        ("ABCDe", -1),
        ("BB", 45),
        ("ABB", 95),
        ("AAA", 130),
        ("AAAB", 160),
        ("AAABB", 175),
        ("ABCABCA", 130 + 45 + 20 + 20)
    ]
)
def test_checkout(skus: str, expected: int):
    assert checkout(skus) == expected


