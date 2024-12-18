import copy

class Guard:
    directions = {"^": "up", ">": "right", "v": "down", "<": "left"}
    def __init__(self, board):
        self.__board = board
        for i, line in enumerate(self.__board):
            if "^" in line:
                self.__char_data = [i, line.index("^")]
        self.__char_data_reset = copy.deepcopy(self.__char_data)
    
    def move(self):
        self.__char_data = copy.deepcopy(self.__char_data_reset)
        repetition = False
        while (not repetition):
            pass

    def add_wall(self):
        pass

    def get_direction(self):
        pass

    def change_direction(self):
        pass
    
    @property
    def board(self):
        for line in self.__board:
            print(line)
        return ""
