from card import Card
from card_repetition import CardRepetition
from hand_type import HandType

class Hand():
    def __init__(self, cards: list[Card]) -> None:
        self.initial_cards: list[Card] = cards
        self.number_of_jacks = len([card for card in cards if card == Card.JACK])
        self.card_repetitions = self.init_card_repetitions_without_jack()
        self.update_card_repetitions_with_best_jack_usage()
        self.simulated_cards = ''.join([card_repetition.repetitions * card_repetition.card.value[0] for card_repetition in self.card_repetitions])
        self.hand_type: HandType = self.get_type()
        self.repr = ''.join([card.value[0] for card in cards])

    def __repr__(self) -> str:
        return self.repr
    
    def __hash__(self) -> int:
        return hash(self.repr)
    
    def __eq__(self, other) -> bool:
        return self.repr == other.repr

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            if self.hand_type < other.hand_type:
                return True
            if other.hand_type < self.hand_type:
                return False
            for i in range(len(self.initial_cards)):
                card = self.initial_cards[i]
                other_card = other.initial_cards[i]
                if card < other_card:
                    return True
                if other_card < card:
                    return False
            return False
        return NotImplemented
    
    def init_card_repetitions_without_jack(self):
        map = {}
        for card in self.initial_cards:
            if card == Card.JACK:
                continue
            if card in map:
                map[card] += 1
            else:
                map[card] = 1

        card_repetitions = []
        for card in map:
            repetitions = map[card]
            card_repetition = CardRepetition(card, repetitions)
            card_repetitions.append(card_repetition)
        card_repetitions.sort()
        return card_repetitions
    
    def update_card_repetitions_with_best_jack_usage(self):
        if len(self.card_repetitions) == 0:
            card_repetition = CardRepetition(Card.ACE, 5)
            self.card_repetitions.append(card_repetition)
            return
        best_card_repetition = self.card_repetitions[0]
        best_card_repetition.repetitions += self.number_of_jacks
    
    def get_type(self):
        number_of_repetitions = len(self.card_repetitions)
        if number_of_repetitions == 1:
            return HandType.FIVE_OF_A_KIND
        if number_of_repetitions == 2:
            if self.card_repetitions[0].repetitions == 4:
                return HandType.FOUR_OF_A_KIND
            return HandType.FULL_HOUSE
        if number_of_repetitions == 3:
            if self.card_repetitions[0].repetitions == 3:
                return HandType.THREE_OF_A_KIND
            return HandType.TWO_PAIRS
        if number_of_repetitions == 4:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD
