from collections import deque

filename = "input.txt"

map = []
sr, sc = (-1, -1)

with open(filename) as text:
    for i,row in enumerate(text):
        if "S" in row: sr, sc = (i,row.index("S"))
        map.append(list(row.strip()))

def p(map):
    for row in map: print(row)

assert len(map) == len(map[0])

size = len(map)
steps = 26501365

assert sr == sc == size // 2
assert steps % size == size // 2

def fill(sr,sc,ss):
    ans = set()
    seen = {(sr,sc)}
    q = deque([(sr, sc, ss)])

    dirs = [(0,1), (0,-1), (1,0), (-1,0)]

    while q:
        r, c, s = q.popleft()

        if s % 2 == 0: ans.add((r,c))

        if s == 0: continue

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= len(map) or nc < 0 or nc >= len(map[0]) or map[nr][nc] == "#" or (nr, nc) in seen:
                continue
            seen.add((nr,nc))
            q.append((nr, nc, s - 1))

    return len(ans)

mapWidth = steps // size - 1

odd = (mapWidth // 2 * 2 + 1) ** 2
even = ((mapWidth + 1) // 2 * 2) ** 2

oddPoints = fill(sr, sc, size * 2 + 1)
evenPoints = fill(sr, sc, size * 2)

tCorner = fill(size - 1, sc, size - 1)
bCorner = fill(0, sc, size - 1)
rCorner = fill(sr, 0, size - 1)
lCorner = fill(sr, size - 1, size - 1)

smallTr = fill(size - 1, 0, size // 2 - 1)
smallBr = fill(0, 0, size // 2 - 1)
smallBl = fill(0, size - 1, size // 2 - 1)
smallTl = fill(size - 1, size - 1, size // 2 - 1)

bigTr = fill(size - 1, 0, size * 3// 2 - 1)
bigBr = fill(0, 0, size * 3 // 2 - 1)
bigBl = fill(0, size - 1, size * 3 // 2 - 1)
bigTl = fill(size - 1, size - 1, size * 3 // 2 - 1)

print(odd * oddPoints +
    even * evenPoints 
    + tCorner + bCorner + rCorner + lCorner + 
    (mapWidth + 1) * (smallBl + smallBr + smallTl + smallTr)
    + mapWidth * (bigBl + bigBr + bigTl + bigTr))