from openFile import openFile
from day6bClass import Guard

data = []
openFile(data, "data/day6test.txt")
guard = Guard(data)
print(guard.board, end="")
