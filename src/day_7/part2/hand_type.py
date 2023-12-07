import enum
from functools import total_ordering

@total_ordering
class HandType(enum.Enum):
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIRS = 5
    ONE_PAIR = 6
    HIGH_CARD = 7

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented