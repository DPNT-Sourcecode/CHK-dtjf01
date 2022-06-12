# noinspection PyShadowingBuiltins,PyUnusedLocal

# bare with me, im on my laptop keyboard so expect many typos!

def compute(x: int, y: int) -> int:
    """Sum two numbers together.
        0-100
    """
    if not isinstance(x, int) or x < 0 or x > 100:
        raise ValueError("x must be between 0-100")

    if not isinstance(y, int) or y < 0 or y > 100:
        raise ValueError("y must be between 0-100")

    return x + y
