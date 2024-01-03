filename = "input.txt"

res = 1
raceTimes = []
records = []

with open(filename) as text:
    for i,row in enumerate(text):

        if i == 0:
            raceTimes = list(map(lambda x: int(x), filter(lambda x: x!= "", row.split(":")[1].strip().split(" "))))
        
        elif i == 1:
            records = list(map(lambda x: int(x), filter(lambda x: x!= "", row.split(":")[1].strip().split(" "))))

for i in range(len(raceTimes)):
    raceTime = raceTimes[i]
    record = records[i]
    nWinning = 0
    for timePressed in range(1, raceTime):
        
        speed = timePressed
        distance = speed * (raceTime - timePressed)
        if distance > record:
            nWinning += 1
    
    res *= nWinning


print(res)