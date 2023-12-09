from engine import Engine

def main():
    test_engine = Engine("src/day_3/data/test_input.txt")
    puzzle_engine = Engine("src/day_3/data/puzzle_input.txt")

    assert test_engine.get_sum_of_parts_next_to_symbols() == 4361, "Wrong value for test input - part 1"
    print(puzzle_engine.get_sum_of_parts_next_to_symbols())

    assert test_engine.get_sum_of_gear_ratios() == 467835, "Wrong value for test input - part 2"
    print(puzzle_engine.get_sum_of_gear_ratios())

if __name__ == '__main__':
    main()