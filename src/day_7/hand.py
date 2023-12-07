from card import Card
from card_repetition import CardRepetition

class Hand():
    def __init__(self, cards: list[Card]) -> None:
        map = {}
        for card in cards:
            if card in map:
                map[card] += 1
            else:
                map[card] = 1

        self.card_repetitions = []
        for card in map:
            repetitions = map[card]
            card_repetition = CardRepetition(card, repetitions)
            self.card_repetitions.append(card_repetition)
        self.card_repetitions.sort()

        self.repr = ''
        for card_repetition in self.card_repetitions:
            self.repr += card_repetition.repetitions * card_repetition.card.value[0]

    def __repr__(self) -> str:
        return self.repr
    
    def __hash__(self) -> int:
        return hash(self.repr)
    
    def __eq__(self, other) -> bool:
        return self.repr == other.repr

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            for i in range(len(self.card_repetitions)):
                card_repetition = self.card_repetitions[i]
                other_card_repetition = other.card_repetitions[i]
                if card_repetition < other_card_repetition:
                    return True
                if other_card_repetition < card_repetition:
                    return False
            return False
        return NotImplemented