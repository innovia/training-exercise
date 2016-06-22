# Copyright (c) 2016 Ami . All rights reserved

from random import random
CANDIDATE_A = "a"
CANDIDATE_B = "b"

def elect_in_region(result, chances):
    if result <= chances:
        return CANDIDATE_A
    else:
        return CANDIDATE_B

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
        elected = elect_in_region(result=random_result, chances=candidate_a_chances[region])
        if elected == CANDIDATE_A:
            candidate_a_elected_count += 1
        else:
            candidate_b_elected_count += 1

    if candidate_a_elected_count > candidate_b_elected_count:
        return CANDIDATE_A
    else:
        return CANDIDATE_B

def simulate_elections(elections_count):
    candidate_a_elections_count = 0
    candidate_b_elections_count = 0

    for i in range(elections_count):
        election_result = simulate_a_single_election()

        if election_result == CANDIDATE_A:
            candidate_a_elections_count += 1
        else:
            candidate_b_elections_count += 1

    print("Candidate A won", candidate_a_elections_count, "times")
    print("Candidate B won", candidate_b_elections_count, "times")

    return {
        "count": elections_count,
        CANDIDATE_A: candidate_a_elections_count,
        CANDIDATE_B: candidate_b_elections_count
    }

def calculate_win_probability(elections_count, candidate_winning_count):
    return float(candidate_winning_count) / elections_count * 100

if __name__ == '__main__':
    elections_result = simulate_elections(10)
    candidate_a_probability_to_win = calculate_win_probability(
        elections_count=elections_result["count"],
        candidate_winning_count=elections_result[CANDIDATE_A]
    )
    candidate_b_probability_to_win = calculate_win_probability(
        elections_count=elections_result["count"],
        candidate_winning_count=elections_result[CANDIDATE_B]
    )
    print("Candidate A probability to win in this election:", candidate_a_probability_to_win)
    print("Candidate B probability to win in this election:", candidate_b_probability_to_win)
