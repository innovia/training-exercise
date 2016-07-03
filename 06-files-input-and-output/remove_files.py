# Copyright (c) 2016 Ami . All rights reserved

import os

def find_files_in_folder(extension, file_max_size, path):
    print(
        "Searching for files with .{extention} extension in \"{path}\""
        " and maximum size of {size}bytes".format(
            extention=extension, path=path, size=file_max_size
        )
    )

    file_list = []

    for current_folder, subfolders, file_names in os.walk(path):
        for file_name in file_names:
            full_path = os.path.join(current_folder, file_name)
            file_size = os.path.getsize(full_path)

            if file_name.lower().endswith(extension) and file_size < file_max_size:
                file_list.append(full_path)

    return file_list

def main():
    pictures_folder_name = "little pics"
    script_folder = os.path.dirname(__file__)
    pictures_full_path = os.path.join(script_folder, pictures_folder_name)

    if not os.path.exists(pictures_full_path):
        print("Could not find the folder at " + pictures_full_path)
        exit(1)

    file_list = find_files_in_folder(path=pictures_full_path, extension="jpg", file_max_size=2000)

    if file_list:
        for file_full_path in file_list:
            print("Deleting {}...".format(file_full_path))
            os.remove(file_full_path)

    else:
        print("Did not find any files matching the criteria in the folder you specified")

if __name__ == "__main__":
    main()
