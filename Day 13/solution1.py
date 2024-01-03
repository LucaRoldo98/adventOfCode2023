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

    # Check horizontal reflection

    nRows = len(field)
    nCols = len(field[0])

    verticalReflection = None
    horizontalRefelection = None

    i = 0

    while i < nRows:
        reflIdx = 0
        currIdx = i
        while i > 0 and reflIdx < currIdx and i < nRows and field[i] == field[currIdx-reflIdx-1]:  # Possible reflection
            reflIdx += 1
            i += 1
        
        if i != 0 and reflIdx == currIdx or i == nRows:
            horizontalRefelection = currIdx
            break

        i += 1

    if horizontalRefelection:
        res += horizontalRefelection * 100

    # Vertical Reflection
    # Transpose the matrix
        
    if not horizontalRefelection:
        
        fieldT = [[row[idx] for row in field] for idx in range(nCols)]

        i = 0

        while i < nCols:
            reflIdx = 0
            currIdx = i
            while i > 0 and reflIdx < currIdx and i < nCols and fieldT[i] == fieldT[currIdx-reflIdx-1]:  # Possible reflection
                reflIdx += 1
                i += 1
            
            if i != 0 and reflIdx == currIdx or i == nCols:
                verticalReflection = currIdx
                break

            i += 1

        if verticalReflection:
            res += verticalReflection

print(res)