filename = "input.txt"

res = 0
cardCount = {}

with open(filename) as text:

    for i,row in enumerate(text):
        currID = i + 1
        row = row.split("|")
        winningNums = []
        for el in row[0].split(":")[1].strip().split(" "):
            if el.isnumeric():
                winningNums.append(int(el))
        
        count = 0
        for el in row[1].strip().split(" "):
            if el.isnumeric() and int(el) in winningNums:
                count += 1
        
        for j in range(count):
            cardCount[currID+j+1] = cardCount.get(currID+j+1, 0) + 1 + cardCount.get(currID, 0)
        
        res += 1 + cardCount.get(currID, 0)

        
print(res)
