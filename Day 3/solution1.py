filename = "input.txt"

symbols = [] # (x,y)

with open(filename) as text:
    
    for i,row in enumerate(text):
        for j,ch in enumerate(row):
            if ch != "." and ch != "\n" and not ch.isalnum():
                symbols.append((i,j))

print(symbols)

res = 0

with open(filename) as text:
    for i,row in enumerate(text):
        j = 0
        while j < len(row):
            if row[j].isnumeric():
                jStart = j
                closeToSimbol = False
                while j < len(row) and row[j].isnumeric() and row[j] != ".":
                    if not closeToSimbol:
                        for symbol in symbols:
                            x, y = symbol
                            if abs(i-x) <= 1 and abs(j-y) <= 1:
                                closeToSimbol = True
                                break
                    j += 1
                num = int(row[jStart:j])
                if closeToSimbol: 
                    res += num
                
            j += 1
    
    print(res)