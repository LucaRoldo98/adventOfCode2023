filename = "input.txt"

moves = []
nodes = {}

with open(filename) as text:
    for i,row in enumerate(text):
        if i == 0:
            for ch in row:
                if ch == "L" or ch == "R":
                    moves.append(ch)
        
        elif row[0].isalnum():
            node = row.split("=")[0].strip()
            options = row.split("=")[1].strip().split(",")
            optionL, optionR = options[0][1:], options[1].strip()[:-1]            
            nodes[node] = (optionL, optionR)

steps = 0
curr = "AAA"
nMoves = len(moves)

while curr != "ZZZ":
    move = moves[steps % nMoves]
    if move == "L":
        curr = nodes[curr][0]
    else:
        curr = nodes[curr][1]
    steps += 1

print(steps)