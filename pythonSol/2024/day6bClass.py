import copy, time, os

class Guard:
    def __init__(self, board):
        self.__board = board
        for i, line in enumerate(self.__board):
            if "^" in line:
                self.__char_data = [i, line.index("^")]
        self.__char_data_reset = copy.deepcopy(self.__char_data)
    
    def move(self):
        self.__char_data = copy.deepcopy(self.__char_data_reset)
        repetition = False
        walls = {}
        while (
                self.__char_data[0] != 0 and
                self.__char_data[0] != (len(self.__board[self.__char_data[0]]) - 1) and
                self.__char_data[1] != 0 and
                self.__char_data[1] != (len(self.__board[self.__char_data[0]]) - 1) 
               ):
            direction, repetition = self.__update_direction(walls)
            if repetition:
                break

            match direction:
                case "down":
                    self.__board[self.__char_data[0]] = self.__board[self.__char_data[0]][0:self.__char_data[1]] + "X" + self.__board[self.__char_data[0]][(self.__char_data[1] + 1):]
                    self.__char_data[0] += 1
                    self.__board[self.__char_data[0]] = self.__board[self.__char_data[0]][0:self.__char_data[1]] + "v" + self.__board[self.__char_data[0]][(self.__char_data[1] + 1):]
                case "up":
                    self.__board[self.__char_data[0]] = self.__board[self.__char_data[0]][0:self.__char_data[1]] + "X" + self.__board[self.__char_data[0]][(self.__char_data[1] + 1):]
                    self.__char_data[0] -= 1
                    self.__board[self.__char_data[0]] = self.__board[self.__char_data[0]][0:self.__char_data[1]] + "^" + self.__board[self.__char_data[0]][(self.__char_data[1] + 1):]
                case "left":
                    self.__board[self.__char_data[0]] = self.__board[self.__char_data[0]][0:self.__char_data[1] - 1] + "<X" + self.__board[self.__char_data[0]][self.__char_data[1]:]
                    self.__char_data[1] -= 1
                case "right":
                    self.__board[self.__char_data[0]] = self.__board[self.__char_data[0]][0:self.__char_data[1]] + "X>" + self.__board[self.__char_data[0]][(self.__char_data[1] + 1):]
                    self.__char_data[1] += 1

            print(self.board)
            time.sleep(0.1)
            os.system("clear")

    def possible_wall_options(self):
        self.move()

    def __get_direction(self):
        match self.__board[self.__char_data[0]][self.__char_data[1]]:
            case "^":
                return "up"
            case "<":
                return "left"
            case ">":
                return "right"
            case "v":
                return "down"

    def __update_direction(self, walls):
        direction = self.__get_direction()
        new_direction = None
        repetitions = False

        match direction:
            case "up":
                if self.__board[self.__char_data[0] - 1][self.__char_data[1]] == "#":  
                    new_direction = "right"
                    if [self.__char_data[0] - 1,[self.__char_data[1]], direction] not in walls:
                        walls.append((self.__char_data[0] - 1, self.__char_data[1], direction))
                    else:
                        repetitions = True
            case "down":
                if self.__board[self.__char_data[0] + 1][self.__char_data[1]] == "#":  
                    new_direction = "left"
                    if [self.__char_data[0] + 1,[self.__char_data[1]], direction] not in walls:
                        walls.append((self.__char_data[0] + 1, self.__char_data[1], direction))
                    else:
                        repetitions = True
            case "right":
                if self.__board[self.__char_data[0]][self.__char_data[1] + 1] == "#":  
                    new_direction = "down"
                    if [self.__char_data[0],[self.__char_data[1] + 1], direction] not in walls:
                        walls.append((self.__char_data[0], self.__char_data[1] + 1, direction))
                    else:
                        repetitions = True
            case "left":
                if self.__board[self.__char_data[0]][self.__char_data[1] - 1] == "#":  
                    new_direction = "up"
                    if [self.__char_data[0],[self.__char_data[1] - 1], direction] not in walls:
                        walls.append((self.__char_data[0], self.__char_data[1] - 1, direction))
                    else:
                        repetitions = True

        if new_direction == None:
            return direction, repetitions
        else:
            return new_direction, repetitions
    
    @property
    def board(self):
        for line in self.__board:
            print(line)
        return ""
