"""
"""

import pytest


with open("10_input.txt", "r") as line_text:

    for line in line_text:

        # Need to remove the newline characters
        line = line.strip().split()


@pytest.mark.parametrize(
    "a,b,isOverlapped",
    [
        ["1-9", "10-20", False],
        ["1-6", "6-6", True],
        ["4-5", "3-9", True],
    ],
)
def test_overlap(a, b, isOverlapped):
    """Test whether our overlap checker runs correctly."""
    ...
