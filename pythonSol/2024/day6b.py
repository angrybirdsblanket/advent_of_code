from day6bClass import Guard
from openFile import openFile

def main():
    data = []
    openFile(data, "data/day6test.txt")

    guard = Guard(data)
    print(guard.possible_positions())

if __name__ == "__main__":
    main()



