filename = "input.txt"

fields = []

with open(filename) as text:
    field = []
    for i,row in enumerate(text):
        if row.strip() == "":
            fields.append(field)
            field = []
        else:
            field.append(list(row.strip()))
    fields.append(field)

res = 0

for field in fields:
    
    nRows = len(field)
    nCols = len(field[0])

    # Check horizontal reflection

    verticalReflection = None
    horizontalRefelection = None

    i = 0
    
    while i < nRows:
        reflIdx = 0
        currIdx = checkIdx = i
        possible = True
        smudged = False
        while i > 0 and reflIdx < currIdx and checkIdx < nRows:  # Possible reflection
            for j in range(len(field[i])):
                if field[checkIdx][j] != field[currIdx-reflIdx-1][j]:
                    if smudged:
                        possible = False
                        break
                    else:
                        smudged = True

            if not possible: break

            reflIdx += 1
            checkIdx += 1
        
        if possible and smudged and i != 0 and (reflIdx == currIdx or checkIdx == nRows):
            horizontalRefelection = currIdx
            res += horizontalRefelection * 100
            break

        i += 1

    # Vertical Reflection
    # Transpose the matrix
        
    if not horizontalRefelection:
        
        fieldT = [[row[idx] for row in field] for idx in range(nCols)]

        i = 0

        while i < nCols:
            reflIdx = 0
            currIdx = checkIdx = i
            possible = True
            smudged = False
            while i > 0 and reflIdx < currIdx and checkIdx < nCols:  # Possible reflection
                for j in range(len(fieldT[i])):
                    if fieldT[checkIdx][j] != fieldT[currIdx-reflIdx-1][j]:
                        if smudged:
                            possible = False
                            break
                        else:
                            smudged = True
                reflIdx += 1
                checkIdx += 1
                
                if not possible: break
            
            if possible and smudged and i != 0 and (reflIdx == currIdx or checkIdx == nCols):
                verticalReflection = currIdx
                res += verticalReflection
                break


            i += 1

    if not horizontalRefelection and not verticalReflection:
        print("\n ", list(map(lambda x: str(x), range(nCols))))
        for idx, row in enumerate(field): print(idx, row)
print(res)