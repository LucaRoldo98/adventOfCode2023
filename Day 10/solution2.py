filename = "input.txt"

map = [] 

import sys

sys.setrecursionlimit(100000000)

with open(filename) as text:
    for i,row in enumerate(text):
        map.append(list(filter(lambda x: x != "\n", row)))

leni = len(map)
lenj = len(map[0])

for i in range(leni):
    for j in range(lenj):
        if map[i][j] == "S":
            startPoint = [i,j]


def dfs(i,j,direction,path): # direciton = u, r, d, l 

    curr = map[i][j]
    path.append((i,j))

    if curr == "S":
        return 

    if curr == "-":
        if direction == "r":
            dfs(i, j+1, "r", path)
        elif direction == "l":
            dfs(i, j-1, "l",path)
    
    elif curr == "|":
        if direction == "u":
            dfs(i-1, j, "u", path)
        elif direction == "d":
            dfs(i+1, j, "d", path)

    elif curr == "L":
        if direction == "l":
            dfs(i-1, j, "u", path)
        elif direction == "d":
            dfs(i, j+1, "r",path)

    elif curr == "J":
        if direction == "d":
            dfs(i, j-1, "l", path)
        elif direction == "r":
            dfs(i-1, j, "u",path)

    elif curr == "7":
        if direction == "r":
            dfs(i+1, j, "d", path)
        elif direction == "u":
            dfs(i, j-1, "l",path)

    elif curr == "F":
        if direction == "u":
            dfs(i, j+1, "r", path)
        elif direction == "l":
            dfs(i+1, j, "d",path)


possibleRoutes = []
pipes = ["-", "|", "L", "7", "F", "J"]

directions = ["u", "r", "d", "l"]

for k, (checki, checkj) in enumerate([[-1,0], [0,1], [1,0], [0,-1]]):
    i, j = startPoint[0] + checki, startPoint[1] + checkj

    if directions[k] == "u" and map[i][j] in ["|", "7", "F"]:
        possibleRoutes.append((i,j,"u"))
    
    elif directions[k] == "r" and map[i][j] in ["-", "7", "J"]:
        possibleRoutes.append((i,j, "r"))
    
    elif directions[k] == "d" and map[i][j] in ["|", "L", "J"]:
        possibleRoutes.append((i,j, "d"))
    
    elif directions[k] == "l" and map[i][j] in ["-", "L", "F"]:
        possibleRoutes.append((i,j, "l"))

for route in possibleRoutes:
    path = []
    dfs(route[0],route[1], route[2], path)
    if path[-1] == "S": break

tiles = 0

for i in range(leni):
    inside = False
    for j in range(lenj):
        
        if (i,j) in path and map[i][j] in ["|", "L", "J"]: # If S has a side facing north, include it in the list
            inside = not inside

        elif inside and (i,j) not in path:
            print(i,j)
            tiles += 1
print(tiles)


