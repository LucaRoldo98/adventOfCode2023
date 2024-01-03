filename = "input.txt"

map = []
startPoint = None

with open(filename) as text:
    for i,row in enumerate(text):
        if "S" in row: startPoint = i,row.index("S")
        map.append(list(row.strip()))

def p(map):
    for row in map: print(row)

possiblePoints = set()
possiblePoints.add(startPoint)

dirs = [(0,1), (0,-1), (1,0), (-1,0)]

for step in range(64):
    newPossiblePoints = set()
    for r, c in possiblePoints:
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(map) and 0 <= nc < len(map[0]) and map[nr][nc] != "#":
                newPossiblePoints.add((nr,nc))

    possiblePoints = newPossiblePoints

print(len(possiblePoints))