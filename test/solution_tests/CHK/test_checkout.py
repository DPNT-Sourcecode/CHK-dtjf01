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

@pytest.mark.parmetrize(
    "skus,expected",
    [
        ("A", 50),
        ("B", 30),
        ("C", 20),
        ("D", 15)
    ]
)
def test_checkout(skus: str, expected: int):
    assert checkout(skus) == expected
