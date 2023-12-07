
from biddings import Biddings

def main():
    test_biddings = Biddings("src/day_7/data/test_input.txt")
    assert test_biddings.get_total_earnings() == 5905, "Wrong earnings for test"
    puzzle_biddings = Biddings("src/day_7/data/puzzle_input.txt")
    print(puzzle_biddings.get_total_earnings())

if __name__ == '__main__':
    main()
