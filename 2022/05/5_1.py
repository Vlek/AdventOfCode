"""
The expedition can depart as soon as the final supplies have been unloaded
from the ships. Supplies are stored in stacks of marked crates, but because the
needed supplies are buried under many other crates, the crates need to be
rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To
ensure none of the crates get crushed or fall over, the crane operator will
rearrange them in a series of carefully-planned steps. After the crates are
rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate
procedure, but they forgot to ask her which crate will end up where, and they
want to be ready to unload them as soon as possible so they can embark.
"""

import re

import pytest


def parseState(state_strings: list[str]) -> list[list[str]]:
    """Takes the initial state and creates lists for stacks."""
    # Note that, while the end of each line in the input file for
    # the initial state of the crate stacks includes the needed
    # whitespace characters, because of how python handles lines,
    # we are stripping away this information. In order to gather
    # the number of columns, the best way that I can come up with
    # is to parse the last stack number at the base.
    number_of_rows: int = int(state_strings[-1].split()[-1])

    result: list[list[str]] = [[] for _ in range(number_of_rows)]

    # We want to go from the bottom and work our way up so that
    # things are in LIFO order if we pop.
    for layer_index in range(len(state_strings) - 2, -1, -1):
        for row in range(number_of_rows):

            # We will pull out just the crate letter, leaving the brackets.
            # For this, we will use the starting point and then add to the
            # index using the zero-based indexing of the range generator.
            crate_column_index: int = row * 4 + 1
            if len(state_strings[layer_index]) >= crate_column_index:
                potential_crate: str = state_strings[layer_index][crate_column_index]

                # The crate can come back "empty", meaning that that stack does
                # not have a crate that that position. We will skip if that's
                # the case.
                if potential_crate != " ":
                    result[row].append(potential_crate)

    return result


crate_movement_notation: str = r"move (?P<num>\d+) from (?P<from>\d+) to (?P<to>\d+)"

with open("5_input.txt", "r") as line_text:

    gathering_initial_state: bool = True
    initial_state: list[str] = []
    crate_stacks: list[list[str]] = []

    for line in line_text:

        # Need to remove the newline characters
        line = line.strip()

        if gathering_initial_state:
            # At the end, there's a blank line before the steps.
            # We will use this as an indicator that we stop gathering init
            # state.
            if line == "":
                gathering_initial_state = False
                crate_stacks = parseState(initial_state)
            else:
                initial_state.append(line)
            continue

        movement_info = re.search(crate_movement_notation, line)

        if not movement_info:
            raise Exception("Necessary movement info not found for line.")

        number_to_move: int = int(movement_info["num"])
        crate_row_from: int = int(movement_info["from"])
        crate_row_to: int = int(movement_info["to"])

        crate_stack_from: list[str] = crate_stacks[crate_row_from - 1]
        crate_stack_to: list[str] = crate_stacks[crate_row_to - 1]

        crate_stack_to = crate_stack_to + crate_stack_from[-number_to_move:]
        crate_stack_from = crate_stack_from[:-number_to_move]

        crate_stacks[crate_row_from - 1] = crate_stack_from
        crate_stacks[crate_row_to - 1] = crate_stack_to

    print(f"Top crates: {[i[-1] for i in crate_stacks]}")


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
