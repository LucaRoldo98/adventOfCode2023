import sympy

filename = "input.txt"

posVel = []

with open(filename) as text:
    for i,row in enumerate(text):
        x = tuple(map(int,row.strip().replace("@", ",").split(",")))
        posVel.append(x)

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []

for sx, sy, sz, vx, vy, vz in posVel[:6]:
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
    
answer = sympy.solve(equations)
print(answer)
print(answer[0][xr] + answer[0][yr] + answer[0][zr])