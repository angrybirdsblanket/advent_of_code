from openFile import data

def diagonalSearch(inputArr, count, direction):
    rows = len(inputArr)
    cols = len(inputArr[0])
    target = "XMAS"
    target_len = len(target)

    for row in range(rows):
        for col in range(cols):
            match = True
            for i in range(target_len):
                new_row, new_col = row, col
                if direction == "downRight":
                    new_row, new_col = row + i, col + i
                elif direction == "upLeft":
                    new_row, new_col = row - i, col - i
                elif direction == "downLeft":
                    new_row, new_col = row + i, col - i
                elif direction == "upRight":
                    new_row, new_col = row - i, col + i
                
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    match = False
                    break
                
                if inputArr[new_row][new_col] != target[i]:
                    match = False
                    break

            if match:
                count += 1

    return count


def linearSearch(inputArr, count, direction):
    rows = len(inputArr)
    cols = len(inputArr[0])
    target = "XMAS"
    target_len = len(target)

    for row in range(rows):
        for col in range(cols):
            for i in range(target_len):
                new_row, new_col = row, col

                match = True
                if direction == "right":
                    new_col += i
                elif direction == "left":
                    new_col -= i 
                elif direction == "up":
                    pass
                elif direction == "down":
                    pass

                if inputArr[new_row][new_col] != target[i]:
                    match = False
                    break
            
                if match:
                    count += 1

    return count

count = 0

count = linearSearch(data, count, "down")
count = linearSearch(data, count, "up")
count = linearSearch(data, count, "left")
count = linearSearch(data, count, "right")
count = diagonalSearch(data, count, "downLeft")
count = diagonalSearch(data, count, "downRight")
count = diagonalSearch(data, count, "upLeft")
count = diagonalSearch(data, count, "upRight")

print(count)
