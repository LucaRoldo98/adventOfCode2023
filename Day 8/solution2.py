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
nMoves = len(moves)
currents = []

for node in nodes:
    if node[-1] == "A":
        currents.append(node)

def areAllFinalNodes(currents):
    for curr in currents:
        if curr[-1] != "Z":
            return False
    return True

while not areAllFinalNodes(currents):
    move = moves[steps % nMoves]
    if move == "L":
        for i in range(len(currents)):
            currents[i] = nodes[currents[i]][0]
    else:
        for i in range(len(currents)):
            currents[i] = nodes[currents[i]][1]
    steps += 1

print(steps)