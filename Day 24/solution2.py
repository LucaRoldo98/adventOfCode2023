filename = "input.txt"

map = []

with open(filename) as text:
    for i,row in enumerate(text):
        map.append(list(row.strip()))
                
nRows = len(map)
nCols = len(map[0])
        
start = (0, map[0].index("."))
end = (nRows-1, map[-1].index("."))
            
dirs = [(-1, 0), (0,1), (1,0), (0,-1)]

points = [start, end]

for r, row in enumerate(map):
    for c, ch in enumerate(row):
        if ch == "#": continue
        neighbors = 0
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < nRows and 0 <= nc < nCols and map[nr][nc] != "#":
                neighbors += 1
        
        if neighbors > 2: 
            points.append((r,c))     
            
graph = {pt: {} for pt in points}            

for sr,sc in points:
    stack = [(0,sr,sc)]
    seen = {(sr,sc)}
    while stack:
        d, r, c = stack.pop()
        
        if (r,c) in points and d != 0:
            graph[(sr,sc)][(r,c)] = d
            continue
        
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc 
            if 0 <= nr < nRows and 0 <= nc < nCols and map[nr][nc] != "#" and (nr,nc) not in seen:
                stack.append((d+1, nr, nc))    
                seen.add((nr,nc))
  
seen = set()
          
def dfs(point):
    
    if point == end: return 0
    m = -float("inf")
    
    seen.add(point)
    for nPoint in graph[point]:
        if nPoint not in seen:
            m = max(m, dfs(nPoint) + graph[point][nPoint])
    seen.remove(point)
    return m
    
print(dfs(start))

    
           