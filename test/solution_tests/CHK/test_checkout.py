import pytest

from solutions.CHK.checkout_solution import checkout



def test_checkout(skus: str, expected: int):
    assert checkout(skus) == expected