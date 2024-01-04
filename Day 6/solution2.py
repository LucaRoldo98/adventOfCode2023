import math

filename = "test.txt"

raceTime = ""
record = ""

with open(filename) as text:
    for i,row in enumerate(text):

        if i == 0:
            for el in list(filter(lambda x: x!= "", row.split(":")[1].strip().split(" "))):
                raceTime += el
            raceTime = int(raceTime)
        
        elif i == 1:
            for el in list(filter(lambda x: x!= "", row.split(":")[1].strip().split(" "))):
                record += el
            record = int(record)



sol1 = (raceTime - math.sqrt(raceTime * raceTime - 4 * (record + 1))) / 2
sol2 = (raceTime + math.sqrt(raceTime * raceTime - 4 * (record + 1))) / 2

res = math.floor(sol2) - math.ceil(sol1) + 1

print(res)

# for timePressed in range(1, raceTime):
    
#     speed = timePressed
#     distance = speed * (raceTime - timePressed)
#     if distance > record:
#         rising = 
#         nWinning += 1

# res *= nWinning


