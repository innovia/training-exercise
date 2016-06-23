# Copyright (c) 2016 Ami . All rights reserved

import csv
import os

def parse_csv(file):
    data = {}

    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for name, score in csv_reader:
            score = int(score)
            if name not in data:
                data[name] = score
            else:
                if score > data[name]:
                    data[name] = score

    return data

def show_high_scores(data):
    print("High Scores:")
    print("-------------")

    for name in sorted(data):
        print(name, data[name])

    print("-------------")

def leader_board(data):
    print("Leader board:")
    print("-------------")
    sorted_data = sorted(data, key=data.get, reverse=True)

    for name in sorted_data:
        print("{position} {name} {score}".format(position=sorted_data.index(name) + 1 , name=name, score=data[name]))

    print("-------------")

def main():
    full_path = os.path.realpath("./scores.csv")
    data = parse_csv(full_path)
    print(data)
    show_high_scores(data)
    leader_board(data)

if __name__ == '__main__':
    main()
