filename = "input.txt"

posVel = []

with open(filename) as text:
    for i,row in enumerate(text):
        x = row.strip().split(" @ ")
        pos = list(map(int, x[0].split(",")))
        vel = list(map(int, x[1].split(",")))
        posVel.append((pos,vel))

collideArea = (200000000000000,400000000000000)

count = 0

for i in range(len(posVel) - 2):
    pos1, vel1 = posVel[i]
    x1, y1, _ = pos1
    vx1, vy1, _ = vel1
        
    for j in range(i+1, len(posVel) - 1):
        pos2, vel2 = posVel[j]
        x2, y2, _ = pos2
        vx2, vy2, _ = vel2
        
        if vx1 * vy2 - vy1 * vx2 == 0:
            continue
        
        s = (vx1 * (y1 - y2) + vy1 * x2 - vy1 * x1) / (vx1 * vy2 - vy1 * vx2)
        t = (x2 - x1 + vx2 * s) / vx1

        x = x1 + vx1 * t
        y = y1 + vy1 * t
        
        if s > 0 and t > 0 and collideArea[0] <= x <= collideArea[1] and collideArea[0] <= y <= collideArea[1]:
            count += 1
            
print(count)
        
        