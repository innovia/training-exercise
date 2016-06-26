# Copyright (c) 2016 Ami . All rights reserved

import os

def find_files_in_folder(path, extension, file_max_size):
    print(
        "Searching for files with .{} extension in \"{}\" and maximum size of {}bytes".format(
            extension, path, file_max_size
        )
    )

    file_list = []

    for current_folder, subfolders, file_names in os.walk(path):
        for file_name in file_names:
            full_path = os.path.abspath(os.path.join(current_folder, file_name))
            file_size = os.path.getsize(full_path)

            if file_name.lower().endswith(extension) and file_size < file_max_size:
                file_list.append(full_path)

    return file_list

def main():
    folder = "little pics"
    script_folder = os.path.dirname(__file__)
    full_path = os.path.join(script_folder, folder)

    if not os.path.exists(full_path):
        print("Could not find the folder at " + full_path)
        exit(1)

    file_list = find_files_in_folder(path=full_path, extension="jpg", file_max_size=2000)

    if file_list:
        for file_name in file_list:
            file_to_be_removed = os.path.join(full_path, file_name)
            print("Deleting {}...".format(file_to_be_removed))
            os.remove(file_to_be_removed)
    else:
        print("Did not find any files matching the criteria in the folder you specified")

if __name__ == "__main__":
    main()
