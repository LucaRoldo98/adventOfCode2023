filename = "input.txt"

numbers=[] # num, x, miny, maxy

with open(filename) as text:
    for i,row in enumerate(text):
        j = 0
        while j < len(row):
            if row[j].isnumeric():
                jStart = j
                while j < len(row) and row[j].isnumeric() and row[j] != ".":
                    j += 1
                num = int(row[jStart:j])
                numbers.append((num, i, jStart, j))
            j += 1

print(numbers)

res = 0

with open(filename) as text:
    
    for i,row in enumerate(text):
        for j,ch in enumerate(row):
            if ch == "*":
                closeParts = []
                for num, nx, nminy, nmaxy in numbers:
                    if abs(i-nx) <= 1 and j in range(nminy-1,nmaxy+1):
                        closeParts.append(num)
                if len(closeParts) == 2:
                    print(closeParts)
                    res += closeParts[0] * closeParts[1]

print(res)
