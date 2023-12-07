import enum
from functools import total_ordering

@total_ordering
class Card(enum.Enum):
    ACE = 'A', 1
    KING = 'K', 2
    QUEEN = 'Q', 3
    TEN = 'T', 4
    NINE = '9', 5
    EIGHT = '8', 6
    SEVEN = '7', 7
    SIX = '6', 8
    FIVE = '5', 9
    FOUR = '4', 10
    THREE = '3', 11
    TWO = '2', 12
    JACK = 'J', 13

    @staticmethod
    def from_str(label):
        if label == 'A':
            return Card.ACE
        if label == 'K':
            return Card.KING
        if label == 'Q':
            return Card.QUEEN
        if label == 'J':
            return Card.JACK
        if label == 'T':
            return Card.TEN
        if label == '9':
            return Card.NINE
        if label == '8':
            return Card.EIGHT
        if label == '7':
            return Card.SEVEN
        if label == '6':
            return Card.SIX
        if label == '5':
            return Card.FIVE
        if label == '4':
            return Card.FOUR
        if label == '3':
            return Card.THREE
        if label == '2':
            return Card.TWO
        else:
            raise NotImplementedError

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value[1] < other.value[1]
        return NotImplemented