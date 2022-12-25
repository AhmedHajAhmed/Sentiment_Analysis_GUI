"""
Doctests for find_indices

>>> find_indices("shiny happy people", "happy")
(6, 11)

>>> find_indices("finals are tiring", "tiring")
(11, 17)

>>> find_indices("no good very bad day", "no good")
(0, 7)
"""
from typing import Tuple


def find_indices(full_string: str, part_str: str) -> Tuple[int, int]:
    """takes in a larger string and smaller string and returns a Tuple of the start and end indices of the smaller
    string within the larger one. The smaller string must be in the larger one"""
    assert part_str in full_string or part_str == ""

    # case of neutral sentiment
    if part_str == "":
        return 0, 1

    # otherwise find the start and end indices
    start = full_string.index(part_str)
    return start, start + len(part_str)
