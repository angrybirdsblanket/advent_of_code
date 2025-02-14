from openFile import openFile
from day6Class import Guard

def main():
    data = []
    #i changed which directory im running the code from day 6 onwards, ignore the missing ../../
    openFile(data, "data/day6test.txt")

    guard = Guard(data)
    guard.move()

    count = 0
    for row in data:
        count += row.count("X")

    print(f"The total number of unique tiles passed is {count + 1}")

if __name__ == "__main__":
    main()

