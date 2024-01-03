filename = "input.txt"

clusters = []
springs = []

with open(filename) as text:
    for i,row in enumerate(text):
        spring, cluster = row.strip().split(" ")
        spring = list("?".join([spring] * 5))
        cluster = ",".join([cluster] * 5)
        cluster = list(map(lambda x: int(x), cluster.split(",")))
        springs.append(spring)
        clusters.append(cluster)

res = 0

# Binary tree, where you split at every ?. Check if it is vaild until ? (check sequences until ?)

def isVaildSpring(spring, clusters, tab="\t", verbose = False):
    if verbose: print(clusters, tab, spring)
    
    if not spring:
        if clusters: return 0 
        else: 
            if verbose: print("Valid")
            return 1
        
    # Caching part
    strClusters = ",".join(map(lambda x: str(x), clusters))
    strSpring = str(spring)
    if (strSpring, strClusters) in cache:
        return cache[(strSpring, strClusters)]
    
    if spring[0] == "?":
        res = isVaildSpring(["."] + spring[1:], clusters, tab, verbose) + isVaildSpring(["#"] + spring[1:], clusters, tab, verbose)    
        cache[(strSpring, strClusters)] = res
        return res
    
    elif spring[0] == ".":
        res = isVaildSpring(spring[1:], clusters, tab + "\t", verbose)
        cache[(strSpring, strClusters)] = res
        return res

    elif spring[0] == "#":
        
        if not clusters:
            cache[(strSpring, strClusters)] = 0
            return 0
        
        seqLen = clusters[0]
        
        if seqLen > len(spring):
            cache[(strSpring, strClusters)] = 0
            return 0

        for i in range(1,seqLen):
            if spring[i] == ".":
                cache[(strSpring, strClusters)] = 0
                return 0

        if seqLen < len(spring) and spring[seqLen] == "#":
            cache[(strSpring, strClusters)] = 0
            return 0
        
        elif seqLen < len(spring)  and spring[seqLen] == "?":
            res = isVaildSpring(["."] + spring[seqLen+1:], clusters[1:], tab, verbose)
            cache[(strSpring, strClusters)] = res
            return res
        
        else: 
            res = isVaildSpring(spring[seqLen:], clusters[1:], tab + "\t", verbose)
            cache[(strSpring, strClusters)] = res
            return res
import time

now = time.time()

for i,spring in enumerate(springs):
    cluster = clusters[i]
    cache = {}
    possibilities = isVaildSpring(spring, cluster, verbose=False)
    print(possibilities)
    res += possibilities

print(res)
print("Exec time", time.time() - now)