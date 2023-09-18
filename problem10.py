# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import time


def job_scheduler(f, n):
    time.sleep(n)
    f()

