# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
#
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

# You should be as efficient with time and space as possible.

class OrderLog:

    def __init__(self, log=None):
        self.log = log

    def record(self, order_id):
        if self.log is None:
            self.log = list()
            self.log.append(order_id)
        else:
            self.log.append(order_id)

    def get_last(self, i):
        return self.log[len(self.log) - 1 - i]
