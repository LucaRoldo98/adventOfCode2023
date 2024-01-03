filename = "input.txt"

galaxy = []

with open(filename) as text:
    for i,row in enumerate(text):
        galaxy.append(list(filter(lambda x: x != "\n", row)))        
# Insert rows
rowsToInsert = []
for i,row in enumerate(galaxy):
    if "#" not in row:
        rowsToInsert.append(i)

lenx = len(galaxy[0])

# Insert columns
colsToInsert = []
for j in range(lenx):
    tmp = []
    for row in galaxy:
        tmp.append(row[j])
    if "#" not in tmp:
        colsToInsert.append(j)

galaxyCoords = []

for i,row in enumerate(galaxy):
    print(row)
    for j,el in enumerate(row):
        if el == "#":
            galaxyCoords.append((i,j))

def computeDistance(ai, aj, bi, bj, emptyRows, emptyColumns):
    expandedDistance = 0
    expansionAddition = 1000000 - 1
    left, right = min(aj, bj), max(aj, bj)
    for col in emptyColumns:
        if left < col and col < right:
            expandedDistance += expansionAddition
    top, bottom = min(ai, bi), max(ai, bi)
    for row in emptyRows:
        if top < row and row < bottom:
            expandedDistance += expansionAddition
    return abs(ai - bi) + abs(aj - bj) + expandedDistance

res = 0

while galaxyCoords:
    gi, gj = galaxyCoords.pop(0)
    for othergi, othergj in galaxyCoords:
        dist = computeDistance(gi,gj,othergi,othergj, rowsToInsert, colsToInsert)
        res += dist

print(res)