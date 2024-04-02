# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative.
#
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#
# Follow-up: Can you do this in O(N) time and constant space?


def find_largest_non_adjacent(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr[0], arr[1])

    arr[0] = max(arr[0], 0)
    arr[1] = max(arr[1], 0)

    for n in range(2, len(arr)):
        arr[n] = max(arr[n - 1], arr[n - 2] + arr[n])

    return arr[len(arr) - 1]


def sum_rec(arr, i):
    if i < 0:
        return 0
    return max(sum_rec(arr, i-2) + arr[i], sum_rec(arr, i-1))


def sum_space_rec(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr[0], arr[1])

    prev_indices_max = list({max(arr[0], 0), max(arr[1], 0)})
    for i in range(2, len(arr)):
        print("i: " + str(i) + " values: " + str(prev_indices_max))
        prev_non_cont_val = prev_indices_max[1]
        prev_indices_max[1] = prev_indices_max[0] + arr[i]
        prev_indices_max[0] = max(prev_indices_max[0], prev_non_cont_val)
    return max(prev_indices_max[0], prev_indices_max[1])



if __name__ == "__main__":
    arr1 = [2, 4, 6, 2, 5]
    arr2 = [5, 1, 1, 5]

    # print(find_largest_non_adjacent(arr1))
    # print(find_largest_non_adjacent(arr2))

    # print(sum_rec(arr1, len(arr1) - 1))
    # print(sum_rec(arr2, len(arr2) - 1))

    print(sum_space_rec(arr1))
    print(sum_space_rec(arr2))
