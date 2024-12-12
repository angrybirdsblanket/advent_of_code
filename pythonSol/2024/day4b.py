from openFile import openFile

def check_X_MAS(input):
    count = 0
    rows = len(input)
    cols = len(input[0])

    for i in range(rows - 2):
        for j in range(cols - 2):
            
            block = splitterFunction(input, i, j)

            if block == None:
                continue

            if block[1][1] == "A":
                upLeft, upRight, downLeft, downRight = block[0][0], block[0][2], block[2][0], block[2][2]
                if all(char in ["M", "S"] for char in [upLeft, upRight, downLeft, downRight]):
                    if upLeft != downRight and upRight != downLeft:
                        count += 1
    return count

def splitterFunction(input, row, col):
    output = []
    
    output.append(input[row][col:col+3])
    output.append(input[row+1][col:col+3])
    output.append(input[row+2][col:col+3])

    return output

def main():
    input = []
    openFile(input, "../../data/day4.txt")

    print(check_X_MAS(input))

    

if __name__ == "__main__":
    main()
