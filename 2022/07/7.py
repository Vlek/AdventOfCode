"""
You can hear birds chirping and raindrops hitting leaves as the expedition
proceeds. Occasionally, you can even hear much louder sounds in the
distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its
communication system. You try to run a system update:

$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device

Perhaps you can delete some files to make space for the update?
"""

import pytest


def recursiveFolderSizeSearch(
    directories: dict[str, list[str]],
    files: dict[str, int],
    startingDirectory: str = "/",
    startingFolderSizes: dict[str, int] = {},
) -> dict[str, int]:
    folderSizes: dict[str, int] = startingFolderSizes

    currentDirSize: int = 0

    for thing in directories[startingDirectory]:
        if thing in files:
            currentDirSize += files[thing]
        else:
            if thing in folderSizes:
                currentDirSize += startingFolderSizes[thing]
            else:
                folderSizes.update(
                    recursiveFolderSizeSearch(directories, files, thing, folderSizes)
                )

            currentDirSize += folderSizes[thing]

    folderSizes[startingDirectory] = currentDirSize

    return folderSizes


with open("7_input.txt", "r") as line_text:

    # Directories have a name and a list of files/folders
    directories: dict[str, list[str]] = {"/": []}

    # It appears based on the input file that all of the files and
    # directories that are given have unique identifiers. Note that
    # this would not work if that was not the case, I would need to
    # pay attention to full paths OR supply my own unique identifiers
    # to them.
    files: dict[str, int] = {}
    current_directory: str = "/"

    for line in line_text:

        # Need to remove the newline characters
        line = line.strip().split()

        # If it's a command,
        if line[0] == "$":
            command: str = line[1]

            if command == "cd":
                directory: str = line[2]

                # If we're directly going back to home,
                if directory == "/":
                    current_directory = "/"
                # If we're traversing back one step,
                elif directory == "..":
                    current_directory = current_directory.rsplit("/", maxsplit=1)[0]

                    # While the above works for most cases, if we're only one
                    # directory down from root, then this will return an empty
                    # string.
                    if current_directory == "":
                        current_directory = "/"

                # Otherwise, we're going on step deeper
                else:
                    # Note that we make folders as they're listed,
                    # so, at this point, we should already have at least
                    # an initialized list for it in our directories.
                    if current_directory == "/":
                        current_directory += f"{directory}"
                    else:
                        current_directory += f"/{directory}"

            elif command == "ls":
                # We're going to ignore this
                pass

        # If it's a folder,
        elif line[0] == "dir":
            directory_name: str = line[1]

            complete_path: str = current_directory

            if current_directory == "/":
                complete_path += directory_name
            else:
                complete_path += f"/{directory_name}"

            if complete_path not in directories[current_directory]:
                directories[current_directory].append(complete_path)

            if complete_path not in directories:
                directories[complete_path] = []

        # Else, it's a file
        else:
            file_name: str = line[1]

            file_path: str = current_directory

            if current_directory == "/":
                file_path += file_name
            else:
                file_path += f"/{file_name}"

            file_size: int = int(line[0])

            files[file_path] = file_size
            directories[current_directory].append(file_path)

# print(directories)

folder_sizes = recursiveFolderSizeSearch(directories, files, "/")
# print(folder_sizes)

# For step 1:
# total_size_of_folders_at_or_under_100k: int = 0

# for folder in folder_sizes:
#     if folder_sizes[folder] <= 100000:
#         total_size_of_folders_at_or_under_100k += folder_sizes[folder]

# print(total_size_of_folders_at_or_under_100k)

# step 2:
total_system_size: int = 70_000_000

current_free_space: int = total_system_size - folder_sizes["/"]
space_needed_for_update: int = 30_000_000 - current_free_space

print(f"Total size of files on device: {folder_sizes['/']}")

print(f"Space needed: {space_needed_for_update}")

big_enough_folders: list[str] = []
for folder in folder_sizes:
    if folder_sizes[folder] >= space_needed_for_update:
        big_enough_folders.append(folder)

# Guessed 3048790, but was too low
# Guessed 3075705, but was too low?!
# Realized I was off by 1 zero, tried 37948890, but too high.
# Realized may have to calculate remaining space, then retried. 24390891 wasn't it.
for f in sorted(big_enough_folders, key=lambda path: folder_sizes[path]):
    print(f"{f}: {folder_sizes[f]}")
# print(folder_sizes[big_enough_folders[0]])


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
