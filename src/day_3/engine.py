from part import Part
from star import Star

class Engine():
    def __init__(self, file_name: str) -> None:
        file = open(file_name, 'r')
        lines = file.readlines()
        self.visual = []
        for line in lines:
            split_line = [c for c in line if c != '\n']
            self.visual.append(split_line)
        self.symbols = self.get_symbols()
        self.parts = self.create_all_parts()
        self.stars = self.create_all_stars()

    def get_symbols(self):
        result = set()
        for line in self.visual:
            for c in line:
                if not c.isnumeric() and c != '.' and c != '\n':
                    result.add(c)
        return result
    
    def create_all_parts(self):
        result = []
        start = -1
        end = -1
        ongoing = False
        for i in range(len(self.visual)):
            for j in range(len(self.visual[i])):
                c = self.visual[i][j]
                if c.isnumeric() and not ongoing:
                        start = j
                        ongoing = True
                elif ongoing and not c.isnumeric():
                        end = j-1
                        figure = int(''.join([self.visual[i][k] for k in range(start, end+1)]))
                        part = Part(figure, i, start, end)
                        result.append(part)
                        ongoing = False
            if ongoing:
                end = len(self.visual[i])-1
                figure = int(''.join([self.visual[i][k] for k in range(start, end+1)]))
                part = Part(figure, i, start, end)
                result.append(part)
                ongoing = False
        return result
    
    def create_all_stars(self):
        result = []
        for i in range(len(self.visual)):
            for j in range(len(self.visual[i])):
                if self.visual[i][j] == '*':
                    result.append(Star(i, j))
        return result

    
    # Diagonals are included
    def is_part_next_to_symbol(self, part: str):
        last_line = len(self.visual) - 1
        last_line_index = len(self.visual[0])-1
        line = part.line
        start = part.start
        end = part.end

        # Left
        if start > 0:
            i = line
            j = start-1
            if self.visual[i][j] in self.symbols:
                return True
        # Right
        if end < last_line_index:
            i = line
            j = end+1
            if self.visual[i][j] in self.symbols:
                return True
        # Above
        if line > 0:
            i = line-1
            # Above left
            if start > 0:
                j = start-1
                if self.visual[i][j] in self.symbols:
                    return True
            # Above middle
            for j in range(start, end+1):
                if self.visual[i][j] in self.symbols:
                    return True
            # Above right
            if end < last_line_index:
                j = end+1
                if self.visual[i][j] in self.symbols:
                    return True
        # Below
        if line < last_line:
            i = line+1
            # Below left
            if start > 0:
                j = start-1
                if self.visual[i][j] in self.symbols:
                    return True
            # Below middle
            for j in range(start, end+1):
                if self.visual[i][j] in self.symbols:
                    return True
            # Below right
            if end < last_line_index:
                j = end+1
                if self.visual[i][j] in self.symbols:
                    return True
        return False
                        
    
    def get_sum_of_parts_next_to_symbols(self):
        return sum([part.figure for part in self.parts if self.is_part_next_to_symbol(part)])
    
    # Diagonals are included
    def is_part_next_to_star(self, part: str, star: Star):
        # Possible positions of star_location compared to part
        # Left
        if star.line == part.line and star.index == part.start-1:
            return True
        # Right
        if star.line == part.line and star.index == part.end+1:
            return True
        # Above
        if star.line == part.line - 1 and star.index in range(part.start-1, part.end+2):
            return True
        # Below
        if star.line == part.line + 1 and star.index in range(part.start-1, part.end+2):
            return True
        return False
    
    def get_sum_of_gear_ratios(self):
        connexions = {}
        for star in self.stars:
            connexions[star] = []
            for part in self.parts:
                if self.is_part_next_to_star(part, star):
                    connexions[star].append(part)
        gears = {star : connexions[star] for star in connexions if len(connexions[star]) == 2}
        return sum([gears[gear][0].figure * gears[gear][1].figure for gear in gears])
