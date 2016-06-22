# Copyright (c) 2016 Ami . All rights reserved

from random import random

def elect_in_region(election, chances):
    if election <= chances:
        return "a"
    else:
        return "b"

def simulate_a_single_election():
    candidate_a_chances = {
        "region1": 87,
        "region2": 65,
        "region3": 17
    }
    candidate_a_elected_count = 0
    candidate_b_elected_count = 0

    for region in candidate_a_chances:
        random_result = int(random() * 100)
        elected = elect_in_region(election=random_result, chances=candidate_a_chances[region])
        if elected == "a":
            candidate_a_elected_count += 1
        else:
            candidate_b_elected_count += 1

    if candidate_a_elected_count > candidate_b_elected_count:
        return "a"
    else:
        return "b"

def simulate_elections(elections_count):
    candidate_a_elections_count = 0
    candidate_b_elections_count = 0

    for i in range(elections_count):
        election_result = simulate_a_single_election()

        if election_result == "a":
            candidate_a_elections_count += 1
        else:
            candidate_b_elections_count += 1

    print("Candidate A won", candidate_a_elections_count, "times")
    print("Candidate B won", candidate_b_elections_count, "times")

    return  {
        "count": elections_count,
        "a": candidate_a_elections_count,
        "b": candidate_b_elections_count
    }


def calculate_probability(elections_count, candidate_winning_count):
    return (float(candidate_winning_count) / float(elections_count)) * 100


if __name__ == '__main__':
    elections_result = simulate_elections(10)

    candidate_a_probability_to_win = calculate_probability(elections_count=elections_result["count"], candidate_winning_count=elections_result["a"])

    candidate_b_probability_to_win = calculate_probability(elections_count=elections_result["count"], candidate_winning_count=elections_result["b"])

    print("Candidate A probability to win in this election:", candidate_a_probability_to_win)

    print("Candidate B probability to win in this election:", candidate_b_probability_to_win)

