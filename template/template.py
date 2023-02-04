"""
This is a template that's used to quickly get into the daily challenges.


"""

import pytest

if __name__ == "__main__":
    with open("input.txt", "r") as line_text:

        for line in line_text:

            # Need to remove the newline characters
            line = line.strip()


@pytest.mark.parametrize(
    "treemap,numVisible",
    [
        [
            [
                "30373",
                "25512",
                "65332",
                "33549",
                "35390",
            ],
            21,
        ],
    ],
)
def test_calcNumVisible(treemap: list[str], numVisible: int) -> None:
    """Test whether maps are parsed and calculated correctly."""
    ...
