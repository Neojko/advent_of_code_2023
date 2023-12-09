import re

NUMBERS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def main():
    test1_lines = get_lines("src/day_1/data/test_input_part_1.txt")
    test2_lines = get_lines("src/day_1/data/test_input_part_2.txt")
    puzzle_lines = get_lines("src/day_1/data/puzzle_input.txt")

    assert get_sum_of_line_digits_part_1(test1_lines) == 142, "Wrong value for test - part 1"
    print("Result puzzle - part 1 " + str(get_sum_of_line_digits_part_1(puzzle_lines)))

    assert get_sum_of_line_digits_part_2(test2_lines) == 281, "Wrong value for test - part 2"
    print("Result puzzle - part 2 " + str(get_sum_of_line_digits_part_2(puzzle_lines)))

def get_lines(file_name: str):
    file = open(file_name, 'r')
    return file.readlines()

def combine_digits_part_1(line: str):
    matches = re.findall(r"\d", line)
    return int(matches[0] + matches[-1])

def get_sum_of_line_digits_part_1(lines: list[str]):

    return sum([combine_digits_part_1(line) for line in lines])

def get_sum_of_line_digits_part_2(lines: list[str]):
    pattern = r"\d|" + '|'.join(NUMBERS.keys()) + r""
    reversed_pattern = r"\d|" + '|'.join([reverse(key) for key in NUMBERS.keys()]) + r""
    result = 0
    for line in lines:
        first_match = get_first_match_part_2(line, pattern)
        last_match = get_last_match_part_2(reverse(line), reversed_pattern)
        result += int(first_match + last_match)
    return result

def reverse(string: str):
    return string[::-1]

def get_first_match_part_2(line: str, pattern):
    match = re.findall(pattern, line)[0]
    return match if match.isnumeric() else NUMBERS[match]

def get_last_match_part_2(reversed_line: str, reversed_pattern):
    match = re.findall(reversed_pattern, reversed_line)[0]
    return match if match.isnumeric() else NUMBERS[reverse(match)]

if __name__ == '__main__':
    main()