from collections import defaultdict
import itertools
from heapq import heappop, heappush

filename = "input.txt"

map = []

# https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes
pq = []  # list of entries arranged in a heap
entry_finder = {}  # mapping of tasks to entries
REMOVED = '<removed-task>'  # placeholder for a removed task
counter = itertools.count()  # unique sequence count


def add_task(task, priority=0):
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)


def remove_task(task):
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

def p(map):
    for row in map:
        print(row)

with open(filename) as text:
    for i,row in enumerate(text):
        map.append(list(row.strip()))

width, height = len(map[0]), len(map)

def isGoingOut(i,j):
    return i < 0 or i >= height or j < 0 or j >= width

directions = {
    "u" : (-1,0),
    "r": (0,1),
    "d" : (1,0),
    "l" : (0,-1)
}

def oppositeDirection(d):
    if d == "u": return "d"
    if d == "d": return "u"
    if d == "r": return "l"
    if d == "l": return "r"
    return None

inf = int(1e15)
targetNode = (height-1, width-1)

dist = defaultdict(lambda: inf)
dist[(0,0)] = 0 
add_task((0,0,"u",0))

for i in range(height):
    for j in range(width):
        for k in range(1,4):
            if (i,j) == (0,0):
                continue        
            if k <= i: add_task((i,j,"d",k), inf)
            if k <= j: add_task((i,j,"r",k), inf)
            if k <= height-1-i: add_task((i,j,"u",k), inf)
            if k <= width-1-j: add_task((i,j,"l",k), inf)

while True:
    i, j, prevDir, prevJump = pop_task()
    if (i,j) == targetNode:
        break
    for d in directions:
        if d != oppositeDirection(prevDir):
            for steps in range(1,4):
                nexti, nextj = i + (directions[d][0] * steps), j + (directions[d][1] * steps)
                if isGoingOut(nexti, nextj) or (prevDir == d and steps > 3 - prevJump):
                    continue
                rowSum = colSum = 0
                for col in range(min(j,nextj)+1, max(j,nextj)+1): rowSum += int(map[nexti][col])
                for row in range(min(i,nexti)+1, max(i,nexti)+1): colSum += int(map[row][nextj])
                nextDist = dist[(i,j)] + rowSum + colSum 
                if nextDist < dist[(nexti, nextj)]:
                    dist[(nexti, nextj)] = nextDist
                    if prevDir == d: pq.append((nexti, nextj, d, steps + prevJump))
                    else: add_task((nexti, nextj, d, steps), nextDist)

p(map)
minPath = dist[targetNode] 
print(minPath)

