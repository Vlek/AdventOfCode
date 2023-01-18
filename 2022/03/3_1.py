"""
"""

character_points: dict[str, int] = {chr(c): c - 96 for c in range(97, 26 + 97)}
character_points.update({chr(c): c - 38 for c in range(65, 26 + 65)})


total_points: int = 0


with open("3_input.txt", "r") as inventories:

    inventories_to_compare: list[set[str]] = []

    for inventory_string in inventories:

        inventory: set[str] = set(inventory_string.strip())

        inventories_to_compare.append(inventory)

        if len(inventories_to_compare) < 3:
            continue

        unique_chars: set[str] = set.intersection(*inventories_to_compare)

        if len(unique_chars) > 1:
            raise Exception(
                "There should only ever be ONE unique char. Got more: "
                + str(unique_chars)
            )

        unique_char = unique_chars.pop()

        total_points += character_points[unique_char]

        inventories_to_compare = []

print(f"The total points for all inventories is: {total_points}")
