# Copyright (c) 2016 Ami . All rights reserved

from random import random
from collections import defaultdict


candidate_a_chances = {
    "region1": 87,
    "region2": 65,
    "region3": 17
}

# defaultdict means that if a key is not found in the dictionary,
# then instead of a KeyError being thrown, a new entry is created
a_voices = defaultdict(int)
b_voices = defaultdict(int)

for e in range(1, 10):
    # voice is made up of random number between 0 and 1
    # and is checked as the poistion in the chances for candidate A
    # i.e: voice 89 is located outside the chances for region1 (87)
    # and will be taken as the voice for candidate B
    voice = int(random() * 100)

    for region in candidate_a_chances:
        if voice <= candidate_a_chances[region]:
            a_voices[region] += 1
        else:
            b_voices[region] += 1


print("voices for candidate A")
print(a_voices)

print("voices for candidate B")
print(b_voices)

simulation