# Given a stream of elements too large to store in memory,
# pick a random element from the stream with uniform probability.

import random


def choose_uniform(large_stream):
    random_element = None

    for i, e in enumerate(large_stream):
        if i == 0:
            random_element = e
        if random.randint(1, i + 1) == 1:
            random_element = e

    return random_element
