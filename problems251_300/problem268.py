# Given a 32-bit positive integer N, determine whether it is a power of four in faster than O(log N) time.
import math


def determine_power_of_four(large_number):

    if (large_number & (large_number - 1)) != 0:
        return False

    return (large_number & 0x55555555) == 0


if __name__ == "__main__":
    print(determine_power_of_four(16))
