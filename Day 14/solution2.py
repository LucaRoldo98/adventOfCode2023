filename = "input.txt"

board = []

def prBoard(board):
    for row in board:
        print(row)

def transpose(board):
    return [[row[idx] for row in board] for idx in range(len(board[0]))]

def tilt(board):
    for row in board:
        i = 1
        while i < len(row):
            if row[i] == "O":
                currIdx = i
                while currIdx > 0 and row[currIdx - 1] == ".":
                    row[currIdx - 1] = "O"
                    row[currIdx] = "."
                    currIdx -= 1
            i += 1

def tiltReverse(board):
    for row in board:
        i = len(row) - 2
        while i >= 0:
            if row[i] == "O":
                currIdx = i
                while currIdx < len(row) - 1 and row[currIdx + 1] == ".":
                    row[currIdx + 1] = "O"
                    row[currIdx] = "."
                    currIdx += 1
            i -= 1

with open(filename) as text:
    for i,row in enumerate(text):
        board.append(list(row.strip()))

boardHeight = len(board)
boardLen = len(board[0])

prevBoards = [board]
loopRange = int(1e9)

for i in range(1, loopRange + 1):
    if i % 100 == 0: print(i)
    board = transpose(board)
    tilt(board) # North
    board = transpose(board)
    tilt(board) # West
    board = transpose(board)
    tiltReverse(board) # South
    board = transpose(board)
    tiltReverse(board) # East

    found = False

    for j,prev in enumerate(prevBoards):
        if board == prev: # Cycle
            found = True
            cycleLen = i - j
            x = ((loopRange - j) % cycleLen)
            board = prevBoards[j+int(x)]
            break

    prevBoards.append(board)

    if found: break


print("End\tcycle len", cycleLen)
prBoard(board)

res = 0

for i, row in enumerate(board):
    for el in row:
        if el == "O":
            res += boardHeight - i

print(res)

    