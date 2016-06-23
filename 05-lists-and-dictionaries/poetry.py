# Copyright (c) 2016 Ami . All rights reserved

from random import choice
import re

class SpeechPart(object):
    def __init__(self, name, count, vocabulary):
        self.name = name
        self.count = count
        self.vocabulary = vocabulary

    def random_words(self):
        words = []

        while True:
            if len(words) == self.count or len(words) == len(self.vocabulary):
                return words
            else:
                selected_word = choice(self.vocabulary)
                if selected_word not in words:
                    words.append(selected_word)

        return words

def make_poem():
    speech_parts = [
        SpeechPart(
            name="verb",
            count=3,
            vocabulary=["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
        ),
        SpeechPart(
            name="adjective",
            count=3,
            vocabulary=["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
        ),
        SpeechPart(
            name="adverb",
            count=1,
            vocabulary=["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
        ),
        SpeechPart(
            name="noun",
            count=3,
            vocabulary=[
                "fossil",
                "horse",
                "aardvark",
                "judge",
                "chef",
                "mango",
                "extrovert",
                "gorilla"
            ]
        ),
        SpeechPart(
            name="preposition",
            count=2,
            vocabulary=[
                "against",
                "after",
                "into",
                "beneath",
                "upon",
                "for",
                "in",
                "like",
                "over",
                "within"
            ]
        )
    ]

    poem_structure = (
        "{A/An} {adjective1} {noun1}\n\n"
        "{A/An} {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2}\n"
        "{adverb1}, the {noun1} {verb2}\n"
        "the {noun2} {verb3} {preposition2} a {adjective3} {noun3}\n"
    )

    transform_dict = {}

    for part in speech_parts:
        selected_words = part.random_words()

        if part.name == 'adjective':
            if re.match('^(a|e|i|a|o|u)', selected_words[0]):
                poem_structure = poem_structure.replace("{A/An}", "An")
            else:
                poem_structure = poem_structure.replace("{A/An}", "A")

        for i in range(part.count):
            transform_dict[part.name + str(i + 1)] = selected_words[i]

    poem = poem_structure.format(**transform_dict)
    # This will change a before adjective that starts with a vowel to an if needed.
    return re.sub('(\sa\s)(a|e|i|a|o|u)', " an \\2", poem)

if __name__ == '__main__':
    print(make_poem())
