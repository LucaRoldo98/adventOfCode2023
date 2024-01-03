from heapq import heappop, heappush

filename = "input.txt"

heatMap = []

with open(filename) as text:
    for i,row in enumerate(text):
        heatMap.append(list(map(int,row.strip())))

width, height = len(heatMap[0]), len(heatMap)

def isGoingOut(i,j):
    return not 0 <= i < height or not 0 <= j < width

def p(map):
    for row in map:
        print(row)

directions = {
    "u" : (-1,0),
    "r": (0,1),
    "d" : (1,0),
    "l" : (0,-1)
}

inf = int(1e15)
targetNode = (height-1, width-1)

seen = set()
pq = [(0,0,0,0,0,0)] # Heap (loss, i, j, di, dj, nconsec)

while pq:
    hl, i, j, di, dj, n = heappop(pq)

    if (i, j, di, dj, n) in seen:
        continue 

    seen.add((i, j, di, dj, n))
    
    if (i,j) == targetNode and n > 3:
        print(hl)
        break


    # Go straight
    if n < 10 and (di, dj) != (0,0):
        ni, nj = i + di, j + dj
        if not isGoingOut(ni, nj): 
            nhl = hl + heatMap[ni][nj]
            heappush(pq, (nhl, ni, nj, di, dj, n + 1))

    # Turn 
    if n == 0 or n > 3:
        for dir in directions:
            ndi, ndj = directions[dir]
            if (ndi, ndj) != (di, dj) and (ndi, ndj) != (-di, -dj):
                ni, nj = i + ndi, j + ndj
                if not isGoingOut(ni, nj): 
                    nhl = hl + heatMap[ni][nj]
                    heappush(pq, (nhl, ni, nj, ndi, ndj, 1))

