# Copyright (c) 2016 Ami . All rights reserved

import os

def find_files_in_folder(path, extention, file_max_size):
    file_list = []

    for current_folder, subfolders, file_names in os.walk(path):
        for file_name in file_names:
            full_path = os.path.abspath(os.path.join(current_folder, file_name))
            file_size = os.path.getsize(full_path)

            if file_name.lower().endswith(extention) and file_size < file_max_size:
                file_list.append(full_path)

    return file_list

def main():
    folder = "./little pics"
    full_path = os.path.abspath(folder)

    if not os.path.exists(full_path):
        print("Could not find the folder at " + full_path)
        exit(1)

    file_list = find_files_in_folder(path=folder, extention="jpg", file_max_size=2000)

    if file_list:
        for file_name in file_list:
            print("Deleting {}...".format(file_name))
            os.remove(full_path)

if __name__ == "__main__":
    main()
