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



nMoves = len(moves)
currents = []

for node in nodes:
    if node[-1] == "A":
        currents.append(node)

lengths = []

for curr in currents:
    steps = 0
    currIter = curr
    while currIter[-1] != "Z":
        move = moves[steps % nMoves]
        if move == "L":
            currIter = nodes[currIter][0]
        else:
            currIter = nodes[currIter][1]
        steps += 1
    
    lengths.append(steps)

print(lengths)

import numpy as np
print(np.lcm.reduce(lengths))