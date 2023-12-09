
class Game():
    def __init__(self, line: str) -> None:
        line_split_semi = line.split(': ')
        self.id = int(line_split_semi[0].split()[1])

        self.red = []
        self.green = []
        self.blue = []
        
        turns = line_split_semi[1].split(';')
        for turn in turns:
            color_infos = turn.split(', ')
            for color_info in color_infos:
                color_info_split = color_info.split()
                number = int(color_info_split[0])
                color = color_info_split[1]
                if color == 'red':
                    self.red.append(number)
                elif color == 'green':
                    self.green.append(number)
                elif color == 'blue':
                    self.blue.append(number)

    def is_possible(self, reds: int, greens: int, blues: int):
        return max(self.red) <= reds and max(self.green) <= greens and max(self.blue) <= blues
    
    def get_power(self):
        return max(self.red) * max(self.green) * max(self.blue)