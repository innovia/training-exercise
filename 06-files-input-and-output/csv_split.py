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
        help="CSV input file",
        required=True
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
        return False
    else:
        return parser.parse_args()

def validate_minimum_rows(csv_file_name, csv_file_num_lines, row_limit):
    print(
        "Validating file {file_name} has more than {row_limit} rows to split by...".format(
            file_name=csv_file_name,
            row_limit=row_limit,
        ),
        end=""
    )
    return row_limit < csv_file_num_lines

def split_csv_to_chunks_by_rows(csv_data, row_limit):
    """
    :param csv_data: csv lines in list.
    :param row_limit: split into a list with max size of row_limit.
    :return: a list of lists (chunks) of csv lines.
    """
    print("Splitting CSV into chunks every " + str(row_limit) + " lines")
    return split_list_in_groups_of(row_limit, csv_data)

def split_list_in_groups_of(group_size, list_to_slice):
    slices = list()
    current_slice = list()

    for index, item in enumerate(list_to_slice):

        if index % group_size == 0:
            current_slice = list()
            slices.append(current_slice)

        current_slice.append(item)

    return slices

def read_file(file_path):
    """
    :return: The output for this is a list of strings.
    """
    with open(file_path, "r") as file_handler:
        return file_handler.readlines()

def save_file(file_path, data):
    with open(file_path, 'w') as file_handler:
        file_handler.writelines(data)

def output_to_files(csv_chunks, output_directory):
    header = csv_chunks[0].pop(0)
    os.makedirs(output_directory, exist_ok=True)

    for chunk_number, chunk in enumerate(csv_chunks):
        chunk.insert(0, header)
        file_name = "csv_part_" + str(chunk_number)
        output_path = os.path.join(output_directory, file_name)
        print("Saving {file_name} with {lines} lines in it".format(
            file_name=output_path,
            lines=len(chunk),
        ))
        save_file(
            file_path=output_path,
            data=chunk,
        )

def main():
    options = get_arguments()
    if options:

        if os.path.exists(options.input_file):
            csv_data = read_file(options.input_file)
            csv_lines = len(csv_data)
            is_valid = validate_minimum_rows(
                csv_file_name=options.input_file,
                csv_file_num_lines=csv_lines,
                row_limit=options.row_limit,
            )
        else:
            print("The file " + options.input_file + " not found")
            return

        if is_valid:
            csv_chunks = split_csv_to_chunks_by_rows(
                csv_data=csv_data,
                row_limit=options.row_limit
            )
            output_to_files(
                csv_chunks=csv_chunks,
                output_directory=options.output_path,
            )
        else:
            print(
                "Error: the file {file_name} contains {file_num_lines} lines, "
                "it is smaller than the {row_limit} rows to split by".format(
                    file_name=options.input_file,
                    file_num_lines=csv_lines,
                    row_limit=options.row_limit,
                )
            )

if __name__ == "__main__":
    main()
