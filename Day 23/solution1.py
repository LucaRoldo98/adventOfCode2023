from heapq import heappop, heappush

filename = "input.txt"

map = []
sr = sc = -1
er = ec = -1

with open(filename) as text:
    for i,row in enumerate(text):
        map.append(list(row.strip()))
                
nRows = len(map)
nCols = len(map[0])
        
for j,ch in enumerate(map[0]):
    if ch == ".":
        sr, sc = (0,j)
        break
    
for j,ch in enumerate(map[nRows - 1]):
    if ch == ".":
        er, ec = (nRows - 1,j)
        break
            
pq = [(0, sr, sc, set())]
dirs = [(-1, 0), (0,1), (1,0), (0,-1)]

pathLengths = []

while pq:
    
    distance, r, c, visited = heappop(pq)
    
    if (r,c) in visited:
        continue
    
    if (r,c) == (er, ec):
        pathLengths.append(distance)
        continue
    
    
    newVisited = visited.copy()
    newVisited.add((r,c))
    
    if map[r][c] == ">":
        heappush(pq, (distance + 1, r, c + 1, newVisited))
    elif map[r][c] == "v":
        heappush(pq, (distance + 1, r + 1, c, newVisited))
    elif map[r][c] == "<":
        heappush(pq, (distance + 1, r, c - 1, newVisited))
    elif map[r][c] == "^":
        heappush(pq, (distance + 1, r - 1, c, newVisited))
    else:
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= nRows or nc < 0 or nc >= nCols or map[nr][nc] == "#" or (nr,nc) in visited:
                continue
            heappush(pq, (distance + 1, nr, nc, newVisited))
        
print(pathLengths) 
print(max(pathLengths))           
        
