filename = "input.txt"

locations = []
seeds = []
maps = []

with open(filename) as text:

    for i,row in enumerate(text):

        if i == 0:
            pair = None 
            for el in row.split(":")[-1].strip().split(" "):
                if not pair:
                    pair = [int(el)]
                else:
                    pair.append(int(el))
                    seeds.append(pair)
                    pair = None
                

        elif row[0].isalpha():
                maps.append([])

        elif row[0].isnumeric():
            maps[-1].append(list(map(lambda x: int(x), row.strip().split(" "))))

for i,map in enumerate(maps):  
    maps[i] = sorted(map, key = lambda x: x[0])

minLocations = []

for seedStart, seedLen in seeds:
    rangesToCheck = [[seedStart, seedStart + seedLen]]
    print("seed", seedStart)
    for map in maps:
        newRanges = []
        print("\tMap", map)
        for dStart, sStart, length in map:
            print("\t\tSubmap", sStart, sStart + length, "Difference", dStart - sStart)
            sEnd = sStart + length
            nToCheck = len(rangesToCheck) 
            rangeIdx = 0
            while rangeIdx < nToCheck:
                incStart, incEnd = rangesToCheck.pop(0)
                print("\t\t\tIncoming", incStart, incEnd)
                if (incStart <= sStart and sStart < incEnd) or (incStart <= sEnd and sEnd < incEnd):
                    newRanges.append([max(sStart, incStart) + (dStart - sStart), min(sEnd, incEnd) + (dStart - sStart)])
                    if incEnd > sEnd:
                        rangesToCheck.append([sEnd, incEnd])

                    if incStart < sStart:
                        rangesToCheck.append([incStart, sStart]) 
                
                elif (incStart >= sStart and incEnd <= sEnd):
                    newRanges.append([incStart + (dStart - sStart), incEnd + (dStart - sStart)])
                
                else:
                    rangesToCheck.append([incStart, incEnd])
                
                rangeIdx += 1
                print("\t\t\tNew", newRanges)
                print("\t\t\tToCheck", rangesToCheck)

        rangesToCheck += newRanges
    
    minLocations.append(min(rangesToCheck, key=lambda x: x[0]))

print(minLocations)
print(min(minLocations), "is the range of lowest locations, so the solution is", min(minLocations)[0])