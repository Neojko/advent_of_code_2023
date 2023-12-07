import enum
from functools import total_ordering

@total_ordering
class Card(enum.Enum):
    ACE = 'A', 1
    KING = 'K', 2
    QUEEN = 'Q', 3
    JACK = 'J', 4
    TEN = 'T', 5
    NINE = '9', 6
    EIGHT = '8', 7
    SEVEN = '7', 8
    SIX = '6', 9
    FIVE = '5', 10
    FOUR = '4', 11
    THREE = '3', 12
    TWO = '2', 13

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