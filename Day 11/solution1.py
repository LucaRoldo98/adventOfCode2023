filename = "test.txt"

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
inserted = 0
for idx in rowsToInsert:
    galaxy.insert(idx + inserted, ["."] * lenx)
    inserted += 1

# Insert columns
colsToInsert = []
for j in range(lenx):
    tmp = []
    for row in galaxy:
        tmp.append(row[j])
    if "#" not in tmp:
        colsToInsert.append(j)

inserted = 0
for idx in colsToInsert:
    for row in galaxy:
        row.insert(idx + inserted, ".")
    inserted += 1

galaxyCoords = []

for i,row in enumerate(galaxy):
    for j,el in enumerate(row):
        if el == "#":
            galaxyCoords.append((i,j))

import math

def computeDistance(ai, aj, bi, bj):
    return abs(ai - bi) + abs(aj - bj)

res = 0

while galaxyCoords:
    gi, gj = galaxyCoords.pop(0)
    for othergi, othergj in galaxyCoords:
        dist = computeDistance(gi,gj,othergi,othergj)
        res += dist

print(res)