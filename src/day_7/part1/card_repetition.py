from card import Card

class CardRepetition():
    def __init__(self, card: Card, repetitions: int) -> None:
        self.card = card
        self.repetitions = repetitions

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            if self.repetitions > other.repetitions:
                return True
            if self.repetitions < other.repetitions:
                return False
            return self.card < other.card
        return NotImplemented