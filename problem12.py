# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb the staircase.
# The order of the steps matters.
#
# For example, if N is 4, then there are 5 unique ways:
#
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2

# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

def climb_one_two_steps(steps_remaining):
    if steps_remaining == 0:
        return 1
    elif steps_remaining == 1:
        return 1
    else:
        return climb_one_two_steps(steps_remaining - 2) + climb_one_two_steps(steps_remaining - 1)


def climb_arbitrary_steps(steps_remaining, possible_steps):
    if steps_remaining == 0:
        return 1
    total_paths = 0
    for i in possible_steps:
        if steps_remaining - i >= 0:
            total_paths += climb_arbitrary_steps(steps_remaining - i, possible_steps)
    return total_paths


if __name__ == "__main__":
    print(climb_one_two_steps(4))
    print(climb_arbitrary_steps(4, {1, 2}))
