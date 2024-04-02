# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

# def retrieve_smallest(arr):
#     array_length = len(arr)
#     for i in range(array_length):
#         val_of_index = arr[i]
#         # If value is greater than the length of the array we can assume there is a missing value before this.
#         # If value is negative we can discard it.
#         if val_of_index > array_length - 1 or val_of_index < 1:
#             arr[i] = -1
#         else:
#             # If value is in the correct place we don't want to replace it
#             if val_of_index != i - 1:
#                 pass
#             # If value of index to swap to is the same we can skip this and keep going
#             elif arr[val_of_index - 1] == val_of_index:
#                 arr[i] = - 1
#             else:
#                 # We must preserve the future value so swap it into the current position
#                 arr[i], arr[val_of_index - 1] = arr[val_of_index - 1], val_of_index
#                 i -= 1


# def retrieve_smallest(arr):
#     for i in range(len(arr)):
#         index_value = arr[i]
#         # Value is in the correct place pass
#         if index_value == i - 1:
#             pass
#         # Remove any indices which are invalid from a sequence perspective
#         if index_value < 1 or index_value > len(arr) - 1:
#             arr[i] = -1
#         # If value to swap equals current value remove the current value
#         elif index_value == arr[arr[i - 1]]:
#             print(arr.pop(i))
#             i -= 1
#         print(arr)

def retrieve_smallest(arr):
    i = 0
    while i < len(arr):
        index_val = arr[i]
        # If value does not fit in the array or is less than one replace the index with -1
        if index_val < 1 or index_val > len(arr) - 1:
            arr[i] = -1
            i += 1
        # If value is in the correct place pass
        elif index_val == i + 1:
            i += 1
            pass
        # If value is not in the correct place then swap it to the correct index
        else:
            arr[i] = arr[index_val - 1]
            arr[index_val - 1] = index_val
    j = 1
    for k in arr:
        if k != j:
            return j
        j += 1
    return j

# [3, 4, -1, 1] i = 0
# -> [-1, 4, 3, 1] i = 0
# -> [-1, 4, 3, 1]
# -> [-1, 1, 3, 4]


if __name__ == "__main__":
    print(retrieve_smallest([3, 4, -1, 1]))
    print(retrieve_smallest([1, 2, 0]))
