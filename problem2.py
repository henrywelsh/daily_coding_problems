# Given an array of integers, return a new array such that
# each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

def productOfAllOtherNumbers(num_list):
    total_product = 1
    for i in num_list:
        total_product *= i
    for j in range(len(num_list)):
        num_list[j] = total_product/num_list[j]
    return num_list


def productOfAllOtherNumbersBonus(num_list):
    product_num_list = num_list.copy()
    for i in range(len(num_list)):
        product_num_list[i] = productOfList(num_list, i)
    return product_num_list


def productOfList(num_list, skip_index):
    final_value = 1
    for i in range(len(num_list)):
        if i != skip_index:
            final_value *= num_list[i]
    return final_value


if __name__ == "__main__":

    # print(productOfAllOtherNumbers([1, 2, 3, 4, 5]))
    # print(productOfAllOtherNumbers([3, 2, 1]))

    print(productOfAllOtherNumbersBonus([1, 2, 3, 4, 5]))
    print(productOfAllOtherNumbersBonus([3, 2, 1]))
