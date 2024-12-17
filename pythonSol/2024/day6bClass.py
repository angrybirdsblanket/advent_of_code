import time, os

class Guard:
    def __init__(self, board):
        self.__board = board
        self.__directions = {"^": "up", ">": "right", "v": "down", "<": "left"}
        for index, line in enumerate(board):
            if "^" in line:
                self.__char_data = [index, line.index("^")]

    def get_char_data(self):
        return self.__char_data

    def __get_direction(self):
        for key, value in self.__directions.items():
            if key == self.__board[self.__char_data[0]][self.__char_data[1]]:
                return value, key
        return 'right', '>' #this line is here because my lsp was getting mad at me for the potential of a "None" result, this however cannot happen so you can ignore this line 


    def change_direction(self, direction, walls):
        repetition = False
        new_direction = direction
        match direction:
            case "up":
                if self.__board[self.__char_data[0] - 1][self.__char_data[1]] == "#" and [self.__char_data[0] - 1,self.__char_data[1]] not in walls:
                    new_direction = "right"
                elif [self.__char_data[0] - 1,self.__char_data[1]] in walls:
                    repetition = True
            case "down":
                if self.__board[self.__char_data[0] + 1][self.__char_data[1]] == "#" and [self.__char_data[0] + 1,self.__char_data[1]] not in walls:
                    new_direction = "left"
                elif [self.__char_data[0] + 1,self.__char_data[1]] in walls:
                    repetition = True
            case "left":
                if self.__board[self.__char_data[0]][self.__char_data[1] - 1] == "#" and [self.__char_data[0],self.__char_data[1] - 1] not in walls:
                    new_direction = "up"
                elif [self.__char_data[0],self.__char_data[1] - 1] in walls:
                    repetition = True
            case "right":
                if self.__board[self.__char_data[0]][self.__char_data[1] + 1] == "#" and [self.__char_data[0],self.__char_data[1] + 1] not in walls:
                    new_direction = "down"
                elif [self.__char_data[0],self.__char_data[1] + 1] in walls:
                    repetition = True

        
        new_arrow = next(key for key, value in self.__directions.items() if value == new_direction)
        return new_direction, new_arrow, repetition


    @property
    def board(self):
        for line in self.__board:
            print(line)
        return ""

    @property
    def char_data(self):
        return self.__char_data

    def set_char_data(self, new_row, new_col):
        self.__char_data[0] = new_row
        self.__char_data[1] = new_col

    def possible_positions(self):
        count = 0
        original_list = self.__board
        for index, line in enumerate(self.__board):
            for i in range(len(line)):
                if line[i] == ".":
                    pass
                    self.__board[index] = self.__board[index][0:i] + "#" + self.__board[index][i + 1:]
                    if self.move():
                        count += 1
                    self.__board = original_list
        return count

    def move(self):
        walls = []
        repetitions = False
        while (
                self.__char_data[0] != len(self.__board) - 1
                and self.__char_data[0] != 0
                and self.__char_data[1] != len(self.__board[0]) -1
                and self.__char_data[1] != 0
                and not repetitions
        ):
            direction, arrow = self.__get_direction()
            direction, arrow, repetitions = self.change_direction(direction, walls)  

            match direction:
                case "up":
                    self.__board[self.__char_data[0]] = (
                        self.__board[self.__char_data[0]][: self.__char_data[1]]
                        + "X"
                        + self.__board[self.__char_data[0]][self.__char_data[1] + 1 :]
                    )
                    self.set_char_data(self.__char_data[0] - 1, self.__char_data[1])
                    self.__board[self.__char_data[0]] = (
                        self.__board[self.__char_data[0]][: self.__char_data[1]]
                        + arrow
                        + self.__board[self.__char_data[0]][self.__char_data[1] + 1 :]
                    )
                case "down":
                    self.__board[self.__char_data[0]] = (
                        self.__board[self.__char_data[0]][: self.__char_data[1]]
                        + "X"
                        + self.__board[self.__char_data[0]][self.__char_data[1] + 1 :]
                    )
                    self.set_char_data(self.__char_data[0] + 1, self.__char_data[1])
                    self.__board[self.__char_data[0]] = (
                        self.__board[self.__char_data[0]][: self.__char_data[1]]
                        + arrow
                        + self.__board[self.__char_data[0]][self.__char_data[1] + 1 :]
                    )
                case "right":
                    self.__board[self.__char_data[0]] = (
                        self.__board[self.__char_data[0]][: self.__char_data[1]]
                        + "X"
                        + self.__board[self.__char_data[0]][self.__char_data[1] + 1 :]
                    )
                    self.set_char_data(self.__char_data[0], self.__char_data[1] + 1)
                    self.__board[self.__char_data[0]] = (
                        self.__board[self.__char_data[0]][: self.__char_data[1]]
                        + arrow
                        + self.__board[self.__char_data[0]][self.__char_data[1] + 1 :]
                    )
                case "left":
                    self.__board[self.__char_data[0]] = (
                        self.__board[self.__char_data[0]][: self.__char_data[1]]
                        + "X"
                        + self.__board[self.__char_data[0]][self.__char_data[1] + 1 :]
                    )
                    self.set_char_data(self.__char_data[0], self.__char_data[1] - 1)
                    self.__board[self.__char_data[0]] = (
                        self.__board[self.__char_data[0]][: self.__char_data[1]]
                        + arrow
                        + self.__board[self.__char_data[0]][self.__char_data[1] + 1 :]
                    )
        if repetitions:
            return True
        else:
            return False

