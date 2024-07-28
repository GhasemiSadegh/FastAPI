from typing import Annotated


def sums(a: Annotated[int, (0, 10)], b: int):
    return a + b