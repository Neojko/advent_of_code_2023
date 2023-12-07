
class Interval():
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return '[' + self.start + ',' + self.end + ']'
    
    def __str__(self) -> str:
        return '[' + self.start + ',' + self.end + ']'

    def is_intersecting(self, other_interval):
        return not (self.start > other_interval.end or other_interval.start > self.end)
    
    # We know that there exists an intersection
    def get_intersection(self, other_interval):
        start = max(self.start, other_interval.start)
        end = min(self.end, other_interval.end)
        return Interval(start, end)
    
    def plus_delta(self, delta):
        return Interval(self.start + delta, self.end + delta)
    
    # We know that the interval is intersected with intersected_interval
    def get_remaining_parts(self, intersected_interval):
        result = []
        if self.start < intersected_interval.start:
            result.append(Interval(self.start, intersected_interval.start - 1))
        if self.end > intersected_interval.end:
            result.append(Interval(intersected_interval.end, self.end - 1))
        return result

class Intervals():
    def __init__(self):
        self.lst = []

    def size(self):
        return len(self.lst)
    
    def add(self, interval: Interval):
        self.lst.append(interval)

    def remove(self, interval: Interval):
        self.lst.remove(interval)

    def sort(self):
        self.lst.sort(key = lambda interval : interval.start)

    def sort_and_merge(self):
        self.sort()
        tmp = []
        for interval in self.lst:
            if tmp and interval.start <= tmp[-1].end:
                tmp[-1].end = max(tmp[-1].end, interval.end)
            else:
                tmp.append(Interval(interval.start, interval.end))
        self.lst = tmp


class IntervalDeltas:
    def __init__(self):
        self.map = {}

    def map_interval_to_delta(self, line: str) -> None:
        split_line = line.split()
        destination_range_start = int(split_line[0])
        source_range_start = int(split_line[1])
        range_length = int(split_line[2])
        delta = destination_range_start - source_range_start
        interval = Interval(source_range_start, source_range_start + range_length)
        self.map[interval] = delta

    def get_delta(self, interval: Interval):
        return self.map[interval]