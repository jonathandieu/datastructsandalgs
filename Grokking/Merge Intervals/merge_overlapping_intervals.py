# Given a list of intervals, merge all the overlapping intervals
# to produce a list that only has mutually exclusive intervals

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start + ", " + str(self.end) + "]", end=''))

def merge(intervals):
    merged = []
    # TODO:
    return merged
