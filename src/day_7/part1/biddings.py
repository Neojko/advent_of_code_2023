from card import Card
from camel_hand import CamelHand

class Biddings():
    def __init__(self, file_name: str) -> None:
        self.map = {}

        file = open(file_name, 'r')
        lines = file.readlines()

        for line in lines:
            split_line = line.split()
            card_lst_string = split_line[0]
            cards = []
            for card_string in card_lst_string:
                card = Card.from_str(card_string)
                cards.append(card)
            hand = CamelHand(cards)
            money = int(split_line[1])
            self.add_bidding(hand, money)

    def add_bidding(self, hand: CamelHand, money: int):
        if hand in self.map:
            raise NotImplementedError
        self.map[hand] = money

    def get_total_earnings(self):
        sorted_list = list(sorted(self.map.keys(), reverse=True))
        result = 0
        for i in range(len(sorted_list)):
            hand = sorted_list[i]
            result += (i + 1) * self.map[hand]
        return result
