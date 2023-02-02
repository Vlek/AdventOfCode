"""
The expedition comes across a peculiar patch of tall trees all planted
carefully in a grid. The Elves explain that a previous expedition planted these
trees as a reforestation effort. Now, they're curious if this would be a good
location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house
hidden. To do this, you need to count the number of trees that are visible
from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height
of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390
"""

import pytest


def calcVisibleTrees(tree_map: list[str]) -> int:
    """Takes a map of tree heights, outputs num visible."""
    result: int
    map_length: int = len(tree_map)
    map_width: int = len(tree_map[0])

    # Because we already know that we can see the trees that are on the
    # outer perimiter, we will set those to true and then only have the
    # trees at least one deep set to false.
    result_map: list[list[bool]] = []

    # Top row
    result_map.append([True] * map_width)

    # All of the middle rows
    for _ in range(map_length - 2):
        result_map.append([True] + [False] * (map_width - 2) + [True])

    # Bottom row
    result_map.append([True] * map_width)

    # Left to right
    for row_index in range(map_length):
        tallest_tree_so_far: int = 0
        for tree_index in range(map_width):
            current_tree_height: int = int(tree_map[row_index][tree_index])

            # We only care if the curret tree is taller than all of those
            # that came before it. Otherwise it is not visible from the
            # outside.
            if current_tree_height > tallest_tree_so_far:
                result_map[row_index][tree_index] = True

                tallest_tree_so_far = current_tree_height

        # If we hit the tallest possible tree, no trees after it will
        # be visible, so we can skip that row.
        if tallest_tree_so_far == 9:
            continue

    # Right to left
    for row_index in range(map_length):
        tallest_tree_so_far = 0
        for tree_index in range(map_width - 1, -1, -1):

            current_tree_height: int = int(tree_map[row_index][tree_index])

            # We only care if the curret tree is taller than all of those
            # that came before it. Otherwise it is not visible from the
            # outside.
            if current_tree_height > tallest_tree_so_far:
                result_map[row_index][tree_index] = True

                tallest_tree_so_far = current_tree_height

        # If we hit the tallest possible tree, no trees after it will
        # be visible, so we can skip that row.
        if tallest_tree_so_far == 9:
            continue

    # Top to bottom
    for tree_index in range(map_width):
        tallest_tree_so_far = 0
        for row_index in range(map_length):

            current_tree_height: int = int(tree_map[row_index][tree_index])

            # We only care if the curret tree is taller than all of those
            # that came before it. Otherwise it is not visible from the
            # outside.
            if current_tree_height > tallest_tree_so_far:
                result_map[row_index][tree_index] = True

                tallest_tree_so_far = current_tree_height

        # If we hit the tallest possible tree, no trees after it will
        # be visible, so we can skip that row.
        if tallest_tree_so_far == 9:
            continue

    # Bottom to top
    for tree_index in range(map_length):
        tallest_tree_so_far = 0
        for row_index in range(map_length - 1, -1, -1):

            current_tree_height: int = int(tree_map[row_index][tree_index])

            # We only care if the curret tree is taller than all of those
            # that came before it. Otherwise it is not visible from the
            # outside.
            if current_tree_height > tallest_tree_so_far:
                result_map[row_index][tree_index] = True

                tallest_tree_so_far = current_tree_height

        # If we hit the tallest possible tree, no trees after it will
        # be visible, so we can skip that row.
        if tallest_tree_so_far == 9:
            continue

    result = sum([sum(i) for i in result_map])

    return result


with open("8_input.txt", "r") as line_text:

    tree_height_map: list[str] = []

    for line in line_text:

        # Need to remove the newline characters
        line = line.strip()

        tree_height_map.append(line)

    print(calcVisibleTrees(tree_height_map))


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
    assert calcVisibleTrees(treemap) == numVisible
