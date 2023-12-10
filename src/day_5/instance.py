from interval import Interval

class Instance():
    def __init__(self, file_name: str) -> None:
        file = open(file_name, 'r')
        lines = file.readlines()

        self.seeds1 = self.create_seeds_for_part_1(lines[0])
        self.seeds2 = self.create_seeds_for_part_2(lines[0])

        self.maps = [{}]
        line_index = 3
        map_index = 0
        while line_index < len(lines):
            line = lines[line_index]
            if line == '\n':
                self.maps.append({})
                map_index += 1
                line_index += 1 # Skipping map header
            else:
                split_line = line.split()
                destination_start = int(split_line[0])
                source_start = int(split_line[1])
                interval_size = int(split_line[2])
                source = Interval(source_start, source_start + interval_size - 1)
                destination = Interval(destination_start, destination_start + interval_size - 1)
                self.maps[map_index][source] = destination
            line_index += 1

    def create_seeds_for_part_1(self, line: str):
        line_split = line.split()
        line_split.pop(0)
        return [int(x) for x in line_split]

    def create_seeds_for_part_2(self, line: str):
        line_split = line.split()
        line_split.pop(0)
        result = []
        number_of_pairs = int(len(line_split) / 2)
        for i in range(number_of_pairs):
            interval_start = int(line_split[2 * i])
            interval_range = int(line_split[2 * i + 1])
            interval_end = interval_start + interval_range - 1
            interval = Interval(interval_start, interval_end)
            result.append(interval)
        return result

    def get_seed_location(self, seed: int):
        result = seed
        for map in self.maps:
            for interval in map:
                if interval.contains(result):
                    delta = result - interval.start
                    result = map[interval].start + delta
                    break
        return result
    
    def get_seed1_with_lowest_location(self):
        return min([self.get_seed_location(seed) for seed in self.seeds1])
    
    def get_seed2_with_lowest_location(self):
        seed_intervals = [interval for interval in self.seeds2]
        new_seed_intervals = []
        for i in range(len(self.maps)):
            map = self.maps[i]
            while len(seed_intervals) > 0:
                seed_interval = seed_intervals[0]
                found_intersection = False
                for source_interval in map:
                    if seed_interval.is_intersecting(source_interval):
                        intersection_interval = seed_interval.get_intersection(source_interval)
                        destination_interval = map[source_interval]
                        delta = destination_interval.start - source_interval.start
                        mapped_intersection_interval = Interval(
                            intersection_interval.start + delta,
                            intersection_interval.end + delta
                        )
                        new_seed_intervals.append(mapped_intersection_interval)
                        if seed_interval != intersection_interval:
                            seed_intervals.extend(seed_interval.get_remaining_parts(intersection_interval))
                        found_intersection = True
                        break
                if not found_intersection:
                    new_seed_intervals.append(seed_interval)
                seed_intervals.remove(seed_interval)
            seed_intervals = [interval for interval in new_seed_intervals]
            new_seed_intervals = []
        return min(interval.start for interval in seed_intervals)
