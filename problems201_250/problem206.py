# A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. 
# For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

# Given an array and a permutation, apply the permutation to the array. 
# For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].


def applyPermutation(currentArray, permutation):
    if len(currentArray) != len(permutation):
        raise ValueError("Lenghts of array and permutation must be equivalent")

    i = 0
    while i < len(permutation):
        if i != permutation[i]:
            val_at_index_i = permutation[i]
            currentArray[i], currentArray[val_at_index_i] = currentArray[val_at_index_i], currentArray[i]
            permutation[i], permutation[val_at_index_i] = permutation[val_at_index_i], permutation[i]
        else:
            i += 1
    return currentArray

if __name__ == "__main__":
   print(applyPermutation(["a", "b", "c"], [2, 1, 0]))