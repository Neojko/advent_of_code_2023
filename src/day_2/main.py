from game import Game

def main():
    test_games = create_games("src/day_2/data/test_input.txt")
    puzzle_games = create_games("src/day_2/data/puzzle_input.txt")

    assert get_sum_possible_game_ids(test_games, 12, 13, 14) == 8, "Wrong value for test input - part 1"
    print(get_sum_possible_game_ids(puzzle_games, 12, 13, 14))

    assert get_sum_game_power(test_games) == 2286, "Wrong value for test input - part 2"
    print(get_sum_game_power(puzzle_games))


def create_games(file_name: str):
    file = open(file_name, 'r')
    lines = file.readlines()
    return [Game(line) for line in lines]

def get_sum_possible_game_ids(games: list[Game], reds: int, greens: int, blues: int):
    return sum([game.id for game in games if game.is_possible(reds, greens, blues)])

def get_sum_game_power(games: list[Game]):
    return sum([game.get_power() for game in games])

if __name__ == '__main__':
    main()