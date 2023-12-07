
from interval_map import IntervalMap

class MapsPartOne():
    def __init__(self, file_name: str):
        file = open(file_name, 'r')
        lines = file.readlines()

        # Seeds
        split_first_line = lines[0].split()
        split_first_line.pop(0)
        self.seeds = [int(x) for x in split_first_line]

        self.interval_maps = [IntervalMap()]

        line_index = 3
        interval_map_index = 0
        while line_index < len(lines):
            line = lines[line_index]
            if line == '\n':
                self.interval_maps.append(IntervalMap())
                interval_map_index += 1
                line_index += 1 # Skipping map header
            else:
                self.interval_maps[interval_map_index].add_line(line)
            line_index += 1
    
    def get_seed_location(self, seed: int):
        result = seed
        for interval_map in self.interval_maps:
            result = interval_map.get_value(result)
        return result
    
    def get_lowest_seed_location(self):
        return min([self.get_seed_location(seed) for seed in self.seeds])


def check_test_input():
    maps = MapsPartOne("src/day_5/data/test.txt")
    assert maps.get_lowest_seed_location() == 35, "Wrong seed location for part 1 test"
        

if __name__ == '__main__':
    check_test_input()
    maps = MapsPartOne("src/day_5/data/puzzle_input.txt")
    print(maps.get_lowest_seed_location())
