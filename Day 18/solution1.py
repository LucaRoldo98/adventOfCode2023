import sys
sys.setrecursionlimit(100000)

filename = "input.txt"

instructions = []

with open(filename) as text:
    for i,row in enumerate(text):
        direction, n, color = row.strip().split()
        instructions.append((direction, int(n), "".join((filter(lambda x: x!="(" and x!=")", list(color))))))

def p(map):
    for row in map: 
        print("".join(row))

# width = height = 100
# currPosition = (width // 2, height // 2)

digged = [(0,0)]
currPosition = (0,0)
limits = (0,0,0,0)

def updateLimits(curr, limits):
    row, col = curr
    minRow, maxRow, minCol, maxCol = limits
    minRow = min(minRow, row)
    maxRow = max(maxRow, row)
    minCol = min(minCol, col)
    maxCol = max(maxCol, col)
    return (minRow, maxRow, minCol, maxCol)

for d, n, color in instructions:
    cr, cc = currPosition
    if d == "R":
        for i in range(cc+1, cc+n+1): 
            digged.append((cr,i))
        currPosition = (cr,cc+n)
    elif d == "L":
        for i in range(cc-1, cc-n-1, -1): 
            digged.append((cr,i))
        currPosition = (cr,cc-n)
    elif d == "U":
        for i in range(cr-1, cr-n-1, -1): 
            digged.append((i,cc))
        currPosition = (cr-n,cc)
    elif d == "D":
        for i in range(cr+1, cr+n+1): 
            digged.append((i,cc))
        currPosition = (cr+n,cc)

    limits = updateLimits(currPosition, limits)

minRow, maxRow, minCol, maxCol = limits

height = maxRow - minRow + 1
width = maxCol - minCol + 1

map = [["." for _ in range(width)] for _ in range(height)]

for r,c in digged:
    map[r-minRow][c-minCol] = "#"

p(map)

# # line rendering
# count = 0
# for i in range(height):
#     inside = False
#     for j in range(width):
#         if map[i][j] == "#": 
#             count += 1
#             inside = not inside
#             continue
        
#         if inside: 
#             count += 1
#             map[i][j] = "#"

# flood fill


def dfs(grid, i, j):
    if i < 0 or  i >= height or j < 0 or j >= width or grid[i][j] == "#":
        return 0
    else: 
        grid[i][j] = "#"
        return 1 + dfs(grid, i+1, j) + dfs(grid, i-1, j) + dfs(grid, i, j+1) + dfs(grid, i, j-1)

# p(map)
print(len(set(digged)) + dfs(map,1,61))