from collections import defaultdict

filename = "input.txt"

bricks = []

with open(filename) as text:
    for i,row in enumerate(text):
        x = row.strip().split("~")
        bricks.append((tuple(map(int, x[0].split(","))), tuple(map(int, x[1].split(",")))))

maxx = max(bricks, key=lambda x: x[1][0])[1][0]
maxy = max(bricks, key=lambda x: x[1][1])[1][1]

bricks = sorted(bricks, key = lambda x: (x[1][2], x[0][2]))

grid = [[(0, -1) for _ in range(maxy + 1)] for _ in range(maxx + 1)]

whosOnBottom = defaultdict(list)
whoseOnTop = defaultdict(list)
essentials = set()

# Compute the falling bricks
for i,(spoint, epoint) in enumerate(bricks): 
    
    sx, sy, sz = spoint
    ex, ey, ez = epoint

    currBottom = 0
    touchBricks = set()

    for x in range(sx, ex + 1):
        for y in range(sy, ey + 1):
            prevHeight, id = grid[x][y] 
            if prevHeight > currBottom:
                touchBricks = set()
                touchBricks.add(id)
                currBottom = prevHeight
            elif prevHeight == currBottom:
                touchBricks.add(id)

    if len(touchBricks) == 1:
        for el in touchBricks:
            essentials.add(el)
    
    for el in touchBricks:
        whosOnBottom[i].append(el)
        whoseOnTop[el].append(i)

    for x in range(sx, ex + 1):
        for y in range(sy, ey + 1):
            grid[x][y] = (currBottom + (ez - sz) + 1, i)

whosOnBottom = dict(whosOnBottom)
whoseOnTop = dict(whoseOnTop)
essentials.remove(-1)
count = 0

for brick in essentials:
    q = whoseOnTop[brick]
    whoWouldFall = set()
    whoWouldFall.add(brick)
    while q:
        curr = q.pop(0)
        if all(x in whoWouldFall for x in whosOnBottom[curr]):
            whoWouldFall.add(curr)
        q += whoseOnTop.get(curr, [])
    count += len(whoWouldFall) - 1    
print(count)


                    
                
        