filename = "input.txt"

instructions = []

with open(filename) as text:
    for i,row in enumerate(text):
        direction, n, color = row.strip().split()
        instructions.append((direction, int(n), "".join((filter(lambda x: x!="(" and x!=")", list(color))))))
 
dirs = {
    0 : (0,1),
    1 : (1,0),
    2 : (0,-1),
    3 : (-1, 0)}

points = [(0,0)]
boundaryPoints = 0

for _, _, color in instructions:
    d = int(color[-1])
    n = int(color[1:-1], 16)
    dr, dc = dirs[d]
    r,c = points[-1]
    n = int(n)
    boundaryPoints += n
    points.append((r + dr * n, c + dc * n))

nPoints = len(points)

A = abs(sum(points[i][0] * (points[i-1][1] - points[(i+1) % nPoints][1]) for i in range(nPoints))) // 2

res = A + boundaryPoints // 2 + 1

print(res)