# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.

def potential_decodings(input_string):
    if len(input_string) == 0 or len(input_string) == 1:
        return 1
    else:
        if int(input_string[0]) > 2:
            return 1 + potential_decodings(input_string[1:])
        else:
            if int(input_string[0]) == 1:
                return potential_decodings(input_string[1:]) + potential_decodings(input_string[2:])
            elif int(input_string[1]) < 7:
                return potential_decodings(input_string[1:]) + potential_decodings(input_string[2:])
            else:
                return potential_decodings(input_string[1:])


if __name__ == "__main__":
    print(potential_decodings('111'))
