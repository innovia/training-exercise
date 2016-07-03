# Copyright (c) 2016 Ami . All rights reserved
import argparse
import csv
import os
import sys

def get_arguments():
    current_directory = os.getcwd()
    parser = argparse.ArgumentParser(description="Split CSV by every x rows")

    parser.add_argument("-i", action="store", dest="input_file", help="CSV input file")
    parser.add_argument("-o", action="store", dest="output_path",
                        help="Output path - where to store the split CSV files",
                        default=current_directory)
    parser.add_argument("-r", action="store", dest="row_limit",
                        help="split by every x lines", type=int, required=True)
    if len(sys.argv) == 1:
        parser.print_help()
        return False
    else:
        return parser.parse_args()

def check_if_file_exists(file):
    if os.path.exists(file):
        return True
    else:
        print("File not found:", file)
        return False

def validate_minimum_rows(file, row_limit):
    print("Validating file {} has more than {} rows to split by...".format(file, row_limit),
        end=""
    )
    file_lines = sum(1 for line in open(file))

    if file_lines < row_limit:
        print(
            "Error: the file {file} contains {file_lines} lines, "
            "it is smaller than the {row_limit} rows to split by".format(
                file=file, file_lines=file_lines, row_limit= row_limit
            )
        )
        return False
    else:
        print("OK")
        print("There are " + str(file_lines) + " lines in the file")
        return True

def split_csv(file, row_limit):
    print("Splitting CSV into chunks every " + str(row_limit) + " lines")
    with open(file, "r") as csv_file:
        csv_data = csv_file.readlines()

    csv_chunks = in_groups_of(row_limit, csv_data)
    return csv_chunks

def in_groups_of(size, list_to_slice):
    slices = list()

    for i, item in enumerate(list_to_slice):
        if i % size == 0:
            current_slice = list()
            current_slice.append(item)
            slices.append(current_slice)
        else:
            current_slice.append(item)

    return slices

def output_to_files(csv_chunks, output_path):
    header = csv_chunks[0].pop(0)

    for index, chunk in enumerate(csv_chunks):
        chunk.insert(0, header)
        output_file= output_path + "/csv_part_" + str(index)
        print("Saving {file_name} with {lines} lines in it".format(
            file_name=output_file, lines=len(chunk)
        ))
        with open(output_file, 'w') as csv_chunk_file:
            csv_chunk_file.writelines(chunk)

def main():
    options = get_arguments()
    if options:
        file_exists = check_if_file_exists(options.input_file)

        if file_exists:
            is_valid = validate_minimum_rows(options.input_file, options.row_limit)
        else:
            is_valid = False

        if is_valid:
            csv_chuncks = split_csv(options.input_file, options.row_limit)
            output_to_files(csv_chuncks, options.output_path)

if __name__ == "__main__":
    main()