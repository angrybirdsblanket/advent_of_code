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
        return 

    def change_direction(self, direction):
        new_direction = direction
        match direction:
            case "up":
                if self.__board[self.__char_data[0] - 1][self.__char_data[1]] == "#":
                    new_direction = "right"
            case "down":
                if self.__board[self.__char_data[0] + 1][self.__char_data[1]] == "#":
                    new_direction = "left"
            case "left":
                if self.__board[self.__char_data[0]][self.__char_data[1] - 1] == "#":
                    new_direction = "up"
            case "right":
                if self.__board[self.__char_data[0]][self.__char_data[1] + 1] == "#":
                    new_direction = "down"

        
        new_arrow = next(key for key, value in self.__directions.items() if value == new_direction)
        return new_direction, new_arrow


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

    def move(self):
        while (
                self.__char_data[0] != len(self.__board) - 1
                and self.__char_data[0] != 0
                and self.__char_data[1] != len(self.__board[0]) -1
                and self.__char_data[1] != 0
        ):
            direction, arrow = self.__get_direction()
            direction, arrow = self.change_direction(direction)  

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


