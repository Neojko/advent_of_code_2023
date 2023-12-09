from math import lcm

class Instance():
    def __init__(self, file_name: str) -> None:
        file = open(file_name, 'r')
        lines = file.readlines()
        self.instructions = lines[0][:-1]
        lines.pop(0)
        lines.pop(0)
        self.next = {}
        for line in lines:
            split_line_equal = line.split('=')
            key = split_line_equal[0][:-1]
            split_line_comma = split_line_equal[1].split(', ')
            left = ''.join(x for x in split_line_comma[0] if x.isalnum())
            right = ''.join(x for x in split_line_comma[1] if x.isalnum())
            self.next[key] = {
                'L': left,
                'R': right
            }

    def get_steps_for_entry_key_and_desired_keys(self, entry_key, desired_keys):
        number_of_steps = 0
        index = 0
        current = entry_key
        while current not in desired_keys:
            instruction = self.instructions[index]
            current = self.next[current][instruction]
            index = index + 1 if index < len(self.instructions)-1 else 0
            number_of_steps += 1
        return number_of_steps
    
    def get_steps(self):
        current = 'AAA'
        desired_keys = ['ZZZ']
        return self.get_steps_for_entry_key_and_desired_keys(current, desired_keys)
    
    def get_simultaneous_steps(self):
        current = [key for key in self.next.keys() if key.endswith('A')]
        desired_keys = [key for key in self.next.keys() if key.endswith('Z')]
        steps = []
        for key in current:
            steps.append(self.get_steps_for_entry_key_and_desired_keys(key, desired_keys))
        return lcm(*steps)

    
    def is_one_key_not_ending_with_Z(self, keys):
        for key in keys:
            if not key.endswith('Z'):
                return True
        return False