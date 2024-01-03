filename = "test.txt"

board = []

def prBoard(board):
    for row in board:
        print(row)

def transpose(board):
    return [[row[idx] for row in board] for idx in range(len(board[0]))]

with open(filename) as text:
    for i,row in enumerate(text):
        board.append(list(row.strip()))

boardHeight = len(board)
boardLen = len(board[0])

boardT = transpose(board)

for row in boardT:
    i = 1
    while i < len(row):
        if row[i] == "O":
            currIdx = i
            while currIdx > 0 and row[currIdx - 1] == ".":
                row[currIdx - 1] = "O"
                row[currIdx] = "."
                currIdx -= 1
        i += 1

res = 0

prBoard(transpose(boardT))

for i, row in enumerate(transpose(boardT)):
    for el in row:
        if el == "O":
            res += boardHeight - i

print(res)

    