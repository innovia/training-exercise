# Copyright (c) 2016 Ami . All rights reserved

import csv
import os

def parse_csv(csv_file):
    data = {}
    with open(csv_file, "r") as csv_file:
        try:
            csv_reader = csv.reader(csv_file)
            for name, score in csv_reader:
                score = int(score)
                data[name] = max(data.get(name), score)
        except ValueError:
            print("Could not parse csv")

    return data

def show_high_scores(data):
    print("High Scores:")
    print("-------------")

    for name in sorted(data):
        print(name, data[name])

def leader_board(data):
    print("Leader board:")
    print("-------------")
    sorted_data = sorted(data, key=data.get, reverse=True)

    for name in sorted_data:
        print("{position} {name} {score}".format(position=sorted_data.index(name) + 1 , name=name, score=data[name]))

def main():
    csv_file = "scores.csv"
    script_folder = os.path.dirname(__file__)
    full_path = os.path.join(script_folder, csv_file)

    if os.path.exists(full_path):
        data = parse_csv(full_path)
        if data:
            show_high_scores(data)
            print()
            leader_board(data)
        else:
            print("Something went wrong with the csv, exiting now")
    else:
        print("CSV file " + full_path + " does not exist")

if __name__ == "__main__":
    main()
