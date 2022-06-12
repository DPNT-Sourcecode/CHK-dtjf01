from typing import Optional
import pytest
from numbers import Number

from solutions.SUM.sum_solution import compute as sum

SUM_CASES = [
    0, 1, 2, 3, 100,
    -1, 101,
    0.1, 0.3, -0.001, 100.001
]


@pytest.fixture
def err(x: Number, y: Number) -> bool:
    err = False
    if not isinstance(x, int) or x < 0 or x > 100:
        err = True

    if not isinstance(y, int) or y < 0 or y > 100:
        err = True

    return err


@pytest.mark.parametrize(
    "x", SUM_CASES
)
@pytest.mark.parametrize(
    "y", SUM_CASES
)
def test_sum(x: Number, y: Number, err: bool):
    if not err:
        assert sum(x, y) == x + y
        return

    with pytest.raises(ValueError):
        sum(x, y)




