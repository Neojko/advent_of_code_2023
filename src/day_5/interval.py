
class Interval():
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return '[' + str(self.start) + ',' + str(self.end) + ']'
    
    def __str__(self) -> str:
        return '[' + self.start + ',' + self.end + ']'
    
    def __hash__(self) -> int:
        return hash(self.__repr__())
    
    def __eq__(self, other) -> int:
        return self.start == other.start and self.end == other.end
    
    def contains(self, number: int):
        return self.start <= number <= self.end

    def is_intersecting(self, other_interval):
        return not (self.start > other_interval.end or other_interval.start > self.end)
    
    # We know that there exists an intersection
    def get_intersection(self, other_interval):
        start = max(self.start, other_interval.start)
        end = min(self.end, other_interval.end)
        return Interval(start, end)
    
    # We know that the interval is intersected with intersected_interval
    def get_remaining_parts(self, intersected_interval):
        result = []
        if self.start < intersected_interval.start:
            result.append(Interval(self.start, intersected_interval.start - 1))
        if self.end > intersected_interval.end:
            result.append(Interval(intersected_interval.end, self.end - 1))
        return result