from cards import Cards

def main():
    test_cards = Cards("src/day_4/data/test_input.txt")
    puzzle_cards = Cards("src/day_4/data/puzzle_input.txt")

    assert test_cards.get_value_part_1() == 13, "Wrong value for test input - part 1"
    print(puzzle_cards.get_value_part_1())

    assert test_cards.get_value_part_2() == 30, "Wrong value for test input - part 2"
    print(puzzle_cards.get_value_part_2())

if __name__ == '__main__':
    main()