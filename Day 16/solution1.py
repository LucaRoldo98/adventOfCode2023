filename = "input.txt"

board = []

with open(filename) as text:
    for i,row in enumerate(text):
        board.append(list(row.strip()))

width, height = len(board[0]), len(board)

moves = set()
beams = [(0,0,"r")] # (i,j, direction) 

def isGoingOut(i,j):
    return i < 0 or i >= height or j < 0 or j >= width

dirIncrements = {
    "u" : (-1,0),
    "r": (0,1),
    "d" : (1,0),
    "l" : (0,-1)
}

def newDirection(mirror, dir):
    newDir = None
    if mirror == "\\":
        if dir == "u": newDir = "l"
        if dir == "r": newDir = "d"
        if dir == "d": newDir = "r"
        if dir == "l": newDir = "u"

    elif mirror == "/":
        if dir == "u": newDir = "r"
        if dir == "r": newDir = "u"
        if dir == "d": newDir = "l"
        if dir == "l": newDir = "d"

    else:
        raise Exception("New direction only accepts '\\' or '/' mirrors")
    return newDir


def move(i,j,dir):
    di, dj = dirIncrements[dir]
    i += di
    j += dj
    return i, j


while beams:
    print(beams)
    newBeams = []
    for beam in beams:
        if beam in moves: # Already seen path
            continue
        moves.add(beam)
        i, j, dir = beam

        if board[i][j] == ".":
            i,j = move(i, j, dir)
            if not isGoingOut(i, j):
                newBeams.append((i,j,dir))
    
        elif board[i][j] == "|":
            if dir == "l" or dir == "r":
                i1, j1 = move(i, j, "u")
                if not isGoingOut(i1, j1):
                    newBeams.append((i1,j1,"u"))
                i2, j2 = move (i, j, "d")
                if not isGoingOut(i2, j2):
                    newBeams.append((i2,j2,"d"))
            else:
                i,j = move(i, j, dir)
                if not isGoingOut(i, j):
                    newBeams.append((i,j,dir))
        
        elif board[i][j] == "-":
            if dir == "u" or dir == "d":
                i1, j1 = move(i, j, "l")
                if not isGoingOut(i1, j1):
                    newBeams.append((i1,j1,"l"))
                i2, j2 = move (i, j, "r")
                if not isGoingOut(i2, j2):
                    newBeams.append((i2,j2,"r"))
            else:
                i,j = move(i, j, dir)
                if not isGoingOut(i, j):
                    newBeams.append((i,j,dir))
        
        elif board[i][j] == "\\" or board[i][j] == "/":
            newDir = newDirection(board[i][j], dir)
            i, j = move(i, j, newDir)
            if not isGoingOut(i, j):
                newBeams.append((i,j,newDir))
            
    beams = newBeams

energized = set()

for i,j,_ in moves:
    energized.add((i,j))
    
res = len(energized)

print(res)

    