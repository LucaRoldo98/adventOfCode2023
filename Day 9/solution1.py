filename = "input.txt"

sequences = []  

with open(filename) as text:
    for i,row in enumerate(text):
        sequences.append(list(map(lambda x: int(x), row.strip().split(" "))))


def allZeros(list):
    for el in list:
        if el != 0:
            return False
    return True

res = 0

for sequence in sequences:
    tree = [sequence]

    while not allZeros(tree[-1]):
        nextSeq = []
        for i in range(1,len(tree[-1])):
            nextSeq.append(tree[-1][i] - tree[-1][i-1])
        tree.append(nextSeq)

        
    extrapolated = 0

    for seq in reversed(tree):
        extrapolated += seq[-1]
    
    res += extrapolated

print(res)

