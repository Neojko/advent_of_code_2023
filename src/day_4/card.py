
class Card():
    def __init__(self, id, winning_numbers: set[int], all_numbers: set[int]) -> None:
        self.id = id
        self.winning_numbers = winning_numbers
        self.all_numbers = all_numbers

    def __repr__(self) -> str:
        return str(self.id)
    
    def __hash__(self) -> int:
        return hash(self.id)

    def get_number_of_owned_winning_numbers(self):
        return len(self.all_numbers.intersection(self.winning_numbers))
    
    def get_value(self):
        owned = self.get_number_of_owned_winning_numbers()
        if owned > 0:
            return pow(2, owned-1)
        return 0
    
    def get_earned_card_ids(self, max_card_id):
        owned = self.get_number_of_owned_winning_numbers()
        return [self.id+i+1 for i in range(owned) if self.id+i+1 <= max_card_id]
