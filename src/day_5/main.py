from instance import Instance

def main():
    test_instance = Instance("src/day_5/data/test_input.txt")
    puzzle_instance = Instance("src/day_5/data/puzzle_input.txt")

    assert test_instance.get_seed1_with_lowest_location() == 35, "Wrong value for test input - part 1"
    print(puzzle_instance.get_seed1_with_lowest_location())

    assert test_instance.get_seed2_with_lowest_location() == 46, "Wrong value for test input - part 2"
    print(puzzle_instance.get_seed2_with_lowest_location())

if __name__ == '__main__':
    main()