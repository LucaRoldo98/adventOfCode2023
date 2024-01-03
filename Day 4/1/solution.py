filename = "input.txt"

res = 0
with open(filename) as text:

    for row in text:
        row = row.split("|")
        winningNums = []
        for el in row[0].split(":")[1].strip().split(" "):
            if el.isnumeric():
                winningNums.append(int(el))
        
        count = 0
        for el in row[1].strip().split(" "):
            if el.isnumeric() and int(el) in winningNums:
                count += 1
        
        if count: res += pow(2,count - 1)
        
print(res)
