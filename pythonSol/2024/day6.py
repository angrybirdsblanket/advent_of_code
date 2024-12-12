from openFile import openFile

class Guard:
    def __init__(self, board):
        self.__directions = {"^": "up", ">": "right", "v": "down", "<": "left"}
        self.__board = board
        for index, line in enumerate(board):
            if "^" in line:
                self.__char_data = [index, line.index("^")]

    def get_char_data(self):
        return self.__char_data

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

    def move_direction(self):
        direction = self.__directions[self.__board[self.__char_data[0]][self.__char_data[1]]]
        character = self.__board[self.__char_data[0]][self.__char_data[1]]
        match direction:
            case "up":

                row_as_list = list(self.__board[self.__char_data[0]])
                row_as_list[self.__char_data[1]] = "X"

                self.__board[self.__char_data[0]] = ''.join(row_as_list)

                self.set_char_data(self.char_data[0] - 1, self.char_data[1])

                row_as_list = list(self.__board[self.__char_data[0]])
                row_as_list[self.__char_data[1]] = f"{self.__directions.keys()}"

                print(self.char_data)
        print(self.board)




def main():
    data = []
    openFile(data, "../../data/day6test.txt")

    guard = Guard(data)
    guard.move_direction()

if __name__ == "__main__":
    main()

