from instance import Instance

def main():
    test_instance1 = Instance("src/day_8/data/test_input_1.txt")
    test_instance2 = Instance("src/day_8/data/test_input_2.txt")
    test_instance3 = Instance("src/day_8/data/test_input_3.txt")
    puzzle_instance = Instance("src/day_8/data/puzzle_input.txt")

    assert test_instance1.get_steps() == 2, "Wrong value for test input 1 - part 1"
    assert test_instance2.get_steps() == 6, "Wrong value for test input 2 - part 1"
    print(puzzle_instance.get_steps())

    assert test_instance3.get_simultaneous_steps() == 6, "Wrong value for test input - part 2"
    print(puzzle_instance.get_simultaneous_steps())

if __name__ == '__main__':
    main()