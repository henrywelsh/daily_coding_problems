# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

def two_num_add(num_list, target_value):
    for i in range(len(num_list)):
        for k in range(i + 1, len(num_list)):
            if num_list[i] + num_list[k] == target_value:
                return True
    return False

def two_num_add_bonus(num_list, target_value):
    possible_solutions = set()
    for i in num_list:
        if i in possible_solutions:
            return True
        else:
            possible_solutions.add(target_value - i)
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(two_num_add([10, 15, 3, 7], 17))
    # print(two_num_add([10, 15, 3, 6], 17))

    print(two_num_add_bonus([10, 15, 3, 7], 17))
    print(two_num_add_bonus([10, 15, 3, 6], 17))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
