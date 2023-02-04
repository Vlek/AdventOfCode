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


def calcMostScenicTreeScore(tree_map: list[str]) -> int:
    """Takes a map of tree heights, outputs num visible."""
    most_scenic_view_score: int = 0

    map_length: int = len(tree_map)
    map_width: int = len(tree_map[0])

    for row_index in range(1, map_length - 1):
        for tree_index in range(1, map_width - 1):
            left_score: int = 0
            right_score: int = 0
            top_score: int = 0
            bottom_score: int = 0

            current_tree_height: int = int(tree_map[row_index][tree_index])

            # Calculate left score:
            for second_tree_index in range(tree_index - 1, -1, -1):
                second_tree_height: int = int(tree_map[row_index][second_tree_index])

                left_score += 1
                if current_tree_height <= second_tree_height:
                    break

            # Calculate right score:
            for second_tree_index in range(tree_index + 1, map_width):
                second_tree_height: int = int(tree_map[row_index][second_tree_index])

                right_score += 1
                if current_tree_height <= second_tree_height:
                    break

            # Calculate bottom score:
            for second_tree_row_index in range(row_index + 1, map_length):
                second_tree_height: int = int(
                    tree_map[second_tree_row_index][tree_index]
                )

                bottom_score += 1
                if current_tree_height <= second_tree_height:
                    break

            # Calculate top score:
            for second_tree_row_index in range(row_index - 1, -1, -1):
                second_tree_height: int = int(
                    tree_map[second_tree_row_index][tree_index]
                )

                top_score += 1
                if current_tree_height <= second_tree_height:
                    break

            current_trees_scenic_score = (
                left_score * right_score * top_score * bottom_score
            )

            if current_trees_scenic_score > most_scenic_view_score:
                most_scenic_view_score = current_trees_scenic_score

    return most_scenic_view_score


with open("8_input.txt", "r") as line_text:

    tree_height_map: list[str] = []

    for line in line_text:

        # Need to remove the newline characters
        line = line.strip()

        tree_height_map.append(line)

    print(calcMostScenicTreeScore(tree_height_map))


@pytest.mark.parametrize(
    "treemap,score",
    [
        [
            [
                "30373",
                "25512",
                "65332",
                "33549",
                "35390",
            ],
            8,
        ],
    ],
)
def test_calcMostScenicTreeScore(treemap: list[str], score: int) -> None:
    """Test whether maps are parsed and calculated correctly."""
    assert calcMostScenicTreeScore(treemap) == score
