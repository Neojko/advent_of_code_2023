from card import Card
from card_repetition import CardRepetition
from hand_type import HandType

class CamelHand():
    def __init__(self, cards: list[Card]) -> None:
        self.cards: list[Card] = cards
        self.hand_type: HandType = self.get_type()
        self.repr = ''
        for card in cards:
            self.repr += card.value[0]

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
            for i in range(len(self.cards)):
                card = self.cards[i]
                other_card = other.cards[i]
                if card < other_card:
                    return True
                if other_card < card:
                    return False
            return False
        return NotImplemented
    
    def get_type(self):
        map = {}
        for card in self.cards:
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

        number_of_repetitions = len(card_repetitions)
        if number_of_repetitions == 1:
            return HandType.FIVE_OF_A_KIND
        if number_of_repetitions == 2:
            if card_repetitions[0].repetitions == 4:
                return HandType.FOUR_OF_A_KIND
            return HandType.FULL_HOUSE
        if number_of_repetitions == 3:
            if card_repetitions[0].repetitions == 3:
                return HandType.THREE_OF_A_KIND
            return HandType.TWO_PAIRS
        if number_of_repetitions == 4:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

