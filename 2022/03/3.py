"""
"""

character_points: dict[str, int] = {chr(c): c - 96 for c in range(97, 26 + 97)}
character_points.update({chr(c): c - 38 for c in range(65, 26 + 65)})


total_points: int = 0


with open("3_input.txt", "r") as inventories:

    for inventory_string in inventories:

        inventory: str = inventory_string.strip()

        # print(inventory)

        # Each compartment is half the size of the inventory
        compartment_size: int = len(inventory) // 2

        compartment_one: set[str] = set(inventory[:compartment_size])
        compartment_two: set[str] = set(inventory[compartment_size:])

        # print(compartment_one)
        # print(compartment_two)

        unique_chars: set[str] = compartment_one.intersection(compartment_two)

        # print(unique_chars)

        if len(unique_chars) > 1:
            raise Exception(
                "There should only ever be ONE unique char. Got more: "
                + str(unique_chars)
            )

        unique_char = unique_chars.pop()

        total_points += character_points[unique_char]

print(f"The total points for all inventories is: {total_points}")
