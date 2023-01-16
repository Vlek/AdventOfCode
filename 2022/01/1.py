"""
Santa's reindeer typically eat regular reindeer food, but they need a lot of
magical energy to deliver presents on Christmas. For that, their favorite snack
is a special type of star fruit that only grows deep in the jungle. The Elves
have brought you on their annual expedition to the grove where the fruit grows.

To supply enough magical energy, the expedition needs to retrieve a minimum of
fifty stars by December 25th. Although the Elves assure you that the grove has
plenty of fruit, you decide to grab any fruit you see along the way, just in
case.

Collect stars by solving puzzles. Two puzzles will be made available on each
day in the Advent calendar; the second puzzle is unlocked when you complete the
first. Each puzzle grants one star. Good luck!

The jungle must be too overgrown and difficult to navigate in vehicles or
access from the air; the Elves' expedition traditionally goes on foot. As your
boats approach land, the Elves begin taking inventory of their supplies. One
important consideration is food - in particular, the number of Calories each
Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the
various meals, snacks, rations, etc. that they've brought with them, one item
per line. Each Elf separates their own inventory from the previous Elf's
inventory (if any) by a blank line.
"""

# Each elf will be kept in order and the sum of their calories
# will be kept in a list.
#
# Initializing with first elf's tracking sum
calories_for_each_elf: list[int] = [0]


with open("1_input.txt", "r") as input_calories:
    for line in input_calories:

        contents = line.strip()

        # If it's the case that we're moving on to the next elf's inventory,
        #
        # Note that the last line of the file has contents. We are not trimming
        # the file itself. Even if it was the case that we were however, that
        # last phantom elf would have an inventory of 0 calories, effectively
        # being thrown out in the check for who has the most.
        if contents == "":
            # Create a new elf's inventory sum
            calories_for_each_elf.append(0)
        else:
            calories_for_each_elf[-1] += int(contents)

    # print(calories_for_each_elf)

    calories_for_each_elf.sort()

    # For the first star,
    highest_calorie_count = calories_for_each_elf[-1]
    print(f"The elf that brought the most calories brought: {highest_calorie_count}")

    # For the second star,
    top_three_calorie_total = sum(calories_for_each_elf[-3:])
    print(
        f"The three elves with the most calories are carrying: {top_three_calorie_total}"
    )
