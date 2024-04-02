# Given an integer, find the next permutation of it in absolute order. 
# For example, given 48975, the next permutation would be 49578.

# Find first case that a value to the left in the integer is greater than the value at the current index
# Find the minimum permutation of those values that increases the value of the integer 

def findNextPermutation(currentInteger : int) :
    digitsInInteger = [int(i) for i in str(currentInteger)]
    n = len(digitsInInteger)
    maxValue = digitsInInteger[n - 1]
    maxValueLocation = n - 1

    for i in range(n - 1, 0, -1):
        if maxValue > digitsInInteger[i]:
            digitsInInteger[maxValueLocation] , digitsInInteger[i] = digitsInInteger[i], digitsInInteger[maxValueLocation]
            return int("".join(map(str, digitsInInteger[:i+1])) + "".join(map(str, sorted(digitsInInteger[i+1:]))))
        if digitsInInteger[i] > maxValue: 
            maxValue = digitsInInteger[i]
    return currentInteger

if __name__ == "__main__":
    print(findNextPermutation(48975))
    print(findNextPermutation(45975))