
class IntervalMap:
    def __init__(self):
        self.map = {}

    def add_line(self, line: list[str]) -> None:
        split_line = line.split()
        destination_range_start = int(split_line[0])
        source_range_start = int(split_line[1])
        range_length = int(split_line[2])
        delta_from_source_to_destination = destination_range_start - source_range_start
        source_range = range(source_range_start, source_range_start + range_length)
        self.map[source_range] = delta_from_source_to_destination
    
    def get_value(self, entry: int):
        for interval in self.map.keys():
            if entry in interval:
                return entry + self.map[interval]
        return entry