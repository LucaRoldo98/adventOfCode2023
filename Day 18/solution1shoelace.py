filename = "input.txt"

instructions = []

with open(filename) as text:
    for i,row in enumerate(text):
        direction, n, color = row.strip().split()
        instructions.append((direction, int(n), "".join((filter(lambda x: x!="(" and x!=")", list(color))))))

dirs = {
    "R" : (0,1),
    "D" : (1,0),
    "L" : (0,-1),
    "U" : (-1, 0)}

points = [(0,0)]
boundaryPoints = 0

for d, n, _ in instructions:
    dr, dc = dirs[d]
    r,c = points[-1]
    n = int(n)
    boundaryPoints += n
    points.append((r + dr * n, c + dc * n))

nPoints = len(points)

A = abs(sum(points[i][0] * (points[i-1][1] - points[(i+1) % nPoints][1]) for i in range(nPoints))) // 2

res = A + boundaryPoints // 2 + 1

print(res)