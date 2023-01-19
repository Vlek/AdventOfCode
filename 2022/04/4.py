"""
Space needs to be cleared before the last supplies can be unloaded from the
ships, and so several Elves have been assigned the job of cleaning up
sections of the camp. Every section has a unique ID number, and each
Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each
other, they've noticed that many of the assignments overlap. To try to quickly
find overlaps and reduce duplicated effort, the Elves pair up and make a big
list of the section assignments for each pair (your puzzle input).
"""

import pytest

num_overlapping_areas: int = 0


def areasOverlap(area_a: str, area_b: str) -> bool:
    """Takes two elf clearings and checks if a is in b or vice versa."""
    a_x, a_y = [int(i) for i in area_a.split("-")]
    b_x, b_y = [int(i) for i in area_b.split("-")]

    return (a_x <= b_x and b_y <= a_y) or (b_x <= a_x and a_y <= b_y)


with open("4_input.txt", "r") as assignment_pairs:

    for assignment_pair in assignment_pairs:

        pair_one, pair_two = assignment_pair.strip().split(",")

        if areasOverlap(pair_one, pair_two):
            num_overlapping_areas += 1

print(f"Num overlapping areas: {num_overlapping_areas}")


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
    assert (
        areasOverlap(
            a,
            b,
        )
        == isOverlapped
    )
