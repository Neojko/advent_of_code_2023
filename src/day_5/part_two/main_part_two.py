
from interval import Interval, Intervals, IntervalDeltas

class MapsPartTwo():
    def __init__(self, file_name: str):
        file = open(file_name, 'r')
        lines = file.readlines()

        # Initial intervals
        print("Creating initial intervals..")
        split_first_line = lines[0].split()
        split_first_line.pop(0)
        self.intervals = Intervals()
        number_of_pairs = int(len(split_first_line) / 2)
        for i in range(number_of_pairs):
            interval_start = int(split_first_line[2 * i])
            interval_range = int(split_first_line[2 * i + 1])
            interval_end = interval_start + interval_range - 1
            interval = Interval(interval_start, interval_end)
            self.intervals.add(interval)

        interval_deltas = IntervalDeltas()
        line_index = 3
        while line_index < len(lines):
            line = lines[line_index]
            if line == '\n':
                self.update_intervals(interval_deltas)
                interval_deltas = IntervalDeltas()
                line_index += 1 # Skipping map header
            else:
                interval_deltas.map_interval_to_delta(line)
            line_index += 1

    def update_intervals(self, interval_deltas: IntervalDeltas):
        print("Updating intervals..")
        new_intervals = Intervals()
        while self.intervals.size() > 0:
            if self.intervals.size() != 8:
                a = 4
            interval = self.intervals.lst[0]
            is_intersection = False
            for entry in interval_deltas.map.items():
                map_interval = entry[0]
                delta = entry[1]
                if interval.is_intersecting(map_interval):
                    is_intersection = True
                    intersection = interval.get_intersection(map_interval)
                    new_intervals.add(intersection.plus_delta(delta))
                    remaining_intervals = interval.get_remaining_parts(intersection)
                    for remaining_interval in remaining_intervals:
                        self.intervals.add(remaining_interval)
                    break
            if not is_intersection:
                new_intervals.add(interval)
            self.intervals.remove(interval)
        new_intervals.sort_and_merge()
        self.intervals = new_intervals
    
    def get_lowest_seed_location(self):
        return min([interval.start for interval in self.intervals.lst])


def check_test_input():
    maps = MapsPartTwo("src/day_5/data/test_input.txt")
    assert maps.get_lowest_seed_location() == 46, "Wrong seed location for part 2 test"
        

if __name__ == '__main__':
    # check_test_input()
    maps = MapsPartTwo("src/day_5/data/puzzle_input.txt")
    print(maps.get_lowest_seed_location())
