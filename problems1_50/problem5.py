# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
#
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    def return_a(a, b):
        return a
    return pair(return_a)


def cdr(pair):
    def return_b(a, b):
        return b
    return pair(return_b)


# Implement car and cdr.
if __name__ == "__main__":
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))