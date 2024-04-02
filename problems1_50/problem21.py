# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
# find the minimum number of rooms required.
#
# For example, given [(30, 75), (0, 50), (60, 150)],
# you should return 2.

def find_min_rooms(time_intervals):
    num_overlaps = [0 for i in range(len(time_intervals))]
    for i in range(0, len(time_intervals)):
        for j in range(i + 1, len(time_intervals)):
            if check_overlap(time_intervals[i], time_intervals[j]):
                num_overlaps[i] += 1
                num_overlaps[j] += 1
                # print("Overlapping: " + str(time_intervals[i]) + ", " + str(time_intervals[j]) + " num overlaps: " + str(num_overlaps))
    return max(num_overlaps)


def check_overlap(ti1, ti2):
    first_interval_start = ti1[0]
    first_interval_stop = ti1[1]
    second_interval_start = ti2[0]
    second_interval_stop = ti2[1]
    return (first_interval_start < second_interval_start < first_interval_stop or
            second_interval_start < first_interval_start < second_interval_stop or
            first_interval_start == second_interval_start)


if __name__ == "__main__":
    print(find_min_rooms([(30, 75), (0, 50), (60, 150)]))
    print(find_min_rooms([(0, 30), (0, 30)]))
