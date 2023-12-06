
"""
Time is expressed in milliseconds
Distance is expressed in millimeters
"""

def main():
    # Tests
    test_time_budgets = [7, 15, 30]
    test_distances_to_beat = [9, 40, 200]
    print("Check with test inputs: " + str(solve_puzzle(test_time_budgets, test_distances_to_beat) == 288))

    # Part 1
    puzzle_time_budgets = [59, 68, 82, 74]
    puzzle_distances_to_beat = [543, 1020, 1664, 1022]
    print("Solution for part 1: " + str(solve_puzzle(puzzle_time_budgets, puzzle_distances_to_beat)))

    # Part 2
    print("Solution for part 2: " + str(get_number_of_better_combinations(59688274, 543102016641022)))

def get_distance(time_budget: int, holding_time: int) -> int:
    speed = holding_time
    return (time_budget - holding_time) * speed

def get_number_of_better_combinations(time_budget: int, distance_to_beat: int):
    result = 0
    for holding_time in range(time_budget):
        if get_distance(time_budget, holding_time) > distance_to_beat:
            result += 1
    return result

def solve_puzzle(time_budgets: list[int], distances_to_beat: list[int]):
    result = 1
    for i in range(len(time_budgets)):
        result *= get_number_of_better_combinations(time_budgets[i], distances_to_beat[i])
    return result

if __name__ == '__main__':
    main()