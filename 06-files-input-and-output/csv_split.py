# Copyright (c) 2016 Ami . All rights reserved
import argparse
import csv
import os
import sys

def get_arguments():
    current_directory = os.getcwd()
    parser = argparse.ArgumentParser(description="Split CSV by every x rows")

    parser.add_argument(
        "-i",
        action="store",
        dest="input_file",
        help="CSV input file"
    )
    parser.add_argument(
        "-o",
        action="store",
        dest="output_path",
        help="Output path - where to store the split CSV files",
        default=current_directory
    )
    parser.add_argument(
        "-r",
        action="store",
        dest="row_limit",
        help="split by every x lines",
        type=int,
        required=True
    )

    if len(sys.argv) == 1:
        parser.print_help()
        return None
    else:
        return parser.parse_args()

def check_if_file_exists(file):
    if os.path.exists(file):
        return True
    else:
        print("File not found:", file)
        return False
def validate_minimum_rows(csv_file_name, csv_file_num_lines, row_limit):
    print(
        "Validating file {file_name} has more than {row_limit} rows to split by...".format(
            file_name=csv_file_name,
            row_limit=row_limit,
        ),
        end=""
    )

    if csv_file_num_lines < row_limit:
        print(
            "Error: the file {file_name} contains {file_num_lines} lines, "
            "it is smaller than the {row_limit} rows to split by".format(
                file=csv_file_name,
                file_num_lines=csv_file_num_lines,
                row_limit= row_limit,
            )
        )
        return False
    else:
        print("OK")
        print("There are " + str(csv_file_num_lines) + " lines in the file")
        return True

def split_csv_to_chunks_by_rows(csv_data, row_limit):
    print("Splitting CSV into chunks every " + str(row_limit) + " lines")

    return split_list_in_groups_of(row_limit, csv_data)

def split_list_in_groups_of(group_size, list_to_slice):
    slices = list()

    for index, item in enumerate(list_to_slice):
        if index % group_size == 0:
            current_slice = list()
            current_slice.append(item)
            slices.append(current_slice)
        else:
            current_slice.append(item)

    return slices

def read_file(file_path):
    with open(file_path, "r") as file_handler:
        return file_handler.readlines()

def save_file(file_path, data):
    with open(file_path, 'w') as file_handler:
        file_handler.writelines(data)

def output_to_files(csv_chunks, output_path):
    header = csv_chunks[0].pop(0)
    os.makedirs(output_path, exist_ok=True)

    for chunk_number, chunk in enumerate(csv_chunks):
        chunk.insert(0, header)
        file_name = "csv_part_" + str(chunk_number)
        output_file = os.path.join(output_path, file_name)
        print("Saving {file_name} with {lines} lines in it".format(
            file_name=output_file,
            lines=len(chunk),
        ))
        save_file(output_file, chunk)

def main():
    options = get_arguments()
    try:
        if options:
            if check_if_file_exists(options.input_file):
                csv_data = read_file(options.input_file)
                csv_lines = len(csv_data)
                is_valid = validate_minimum_rows(
                    csv_file_name=options.input_file,
                    csv_file_num_lines=csv_lines,
                    row_limit=options.row_limit,
                )
            else:
                is_valid = False

            if is_valid:
                csv_chunks = split_csv_to_chunks_by_rows(csv_data, options.row_limit)
                output_to_files(csv_chunks, options.output_path)
    except Exception as e:
        print("Something went wrong - {}".format(e))

if __name__ == "__main__":
    main()
