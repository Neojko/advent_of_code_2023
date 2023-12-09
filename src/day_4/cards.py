from card import Card

class Cards():
    def __init__(self, file_name: str) -> None:
        file = open(file_name, 'r')
        lines = file.readlines()
        self.cards = []
        for line in lines:
            split_line_id = line.split(': ')
            id = int(split_line_id[0].split()[1])
            split_line_winning_all = split_line_id[1].split(' | ')
            winning = {int(x) for x in split_line_winning_all[0].split()}
            all = {int(x) for x in split_line_winning_all[1].split()}
            card = Card(id, winning, all)
            self.cards.append(card)
    
    def get_value_part_1(self):
        return sum([card.get_value() for card in self.cards])
    
    def get_value_part_2(self):
        max_card_id = max([card.id for card in self.cards])
        map_card_id_to_card = {card.id : card for card in self.cards}
        number_of_copies = {card : 1 for card in self.cards}
        for card in self.cards:
            earned_card_ids = card.get_earned_card_ids(max_card_id)
            number_of_card_copies = number_of_copies[card]
            for earned_card_id in earned_card_ids:
                earned_card = map_card_id_to_card[earned_card_id]
                number_of_copies[earned_card] += number_of_card_copies
        return sum([number_of_copies[card] for card in number_of_copies])