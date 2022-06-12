from typing import Optional
import pytest
from numbers import Number

from solutions.SUM import sum_solution


@pytest.fixture
def err(x: Number, y: Number) -> bool:


@pytest.mark.parametrize(
    "x", SUM_CASES
)
@pytest.mark.parametrize(
    "y", SUM_CASES
)
def test_sum(x: number, y: number, err: bool):
    if not err:
        assert sum(x, y) == x + y
        return

    with pytest.raises(ValueError):
        sum(x, y)

