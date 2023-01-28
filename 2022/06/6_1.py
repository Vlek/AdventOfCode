"""

Tried 2772, was too low.
"""

import pytest

with open("6_input.txt", "r") as line_text:

    # Need to remove the newline characters
    buffer = line_text.readline().strip()

    for index in range(3, len(buffer)):

        characters_to_check: str = buffer[index : index + 14]
        character_set: set[str] = set(characters_to_check)

        # print(characters_to_check)
        # print(character_set)
        # break

        if len(character_set) == 14:
            print(characters_to_check)
            print(character_set)
            print(f"The first portion with dissimilar items is {index}")
            break


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
