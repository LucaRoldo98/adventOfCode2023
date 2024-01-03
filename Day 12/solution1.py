filename = "input.txt"

springs = []
clusters = []

with open(filename) as text:
    for i,row in enumerate(text):
        spring, cluster = row.strip().split(" ")
        cluster = list(map(lambda x: int(x), cluster.split(",")))
        springs.append(spring)
        clusters.append(cluster)

res = 0

def binaryAdd(seq):
    if seq == ["#" for _ in seq]:
        return False
    idx = -1
    while seq[idx] == "#":
        seq[idx] = "."
        idx -= 1
    seq[idx] = "#"
    return seq    

# Brute force
for idx, spring in enumerate(springs):
    print(spring)
    cluster = clusters[idx]
    questionMarks = []
    for i,l in enumerate(spring):
        if l == "?":
            questionMarks.append(i)

    # Brute force
    carry = False
    springTmp = list(spring)
    toTest = ["."] * len(questionMarks)
    possibilities = 0
    while toTest:
        for i,ch in enumerate(toTest):
            springTmp[questionMarks[i]] = ch
        possible = True
        seq = 0
        patternIdx = 0
        for ch in springTmp:
            if ch == "#":
                seq += 1
            elif seq:
                if patternIdx < len(cluster) and cluster[patternIdx] == seq:
                    patternIdx += 1
                    seq = 0
                else:
                    possible = False
                    break

        if seq:
            if patternIdx < len(cluster) and cluster[patternIdx] == seq:
                patternIdx += 1
            else:   
                possible = False

        if possible and patternIdx == len(cluster):
            possibilities += 1

        toTest = binaryAdd(toTest)

    print(possibilities)
    res += possibilities

print(res)

