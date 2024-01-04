filename = "input.txt"

locations = []
seeds = []
seedToSoil = {} # 0
soilToFertilizer = {}
fertilizerToWater = {}
waterToLight = {}
lightToTemperature = {}
temperatureToHumidity = {}
humidityToLocation = {} # 6

maps = []

with open(filename) as text:

    for i,row in enumerate(text):

        if i == 0:
            for el in row.split(":")[-1].strip().split(" "):
                seeds.append(int(el))

        elif row[0].isalpha():
                maps.append([])

        elif row[0].isnumeric():
            maps[-1].append(list(map(lambda x: int(x), row.strip().split(" "))))
        
for i,seed in enumerate(seeds):
    key = seed
    for map in maps:
        for dStart, sStart, length in map:
            if key >= sStart and key < sStart + length:
                key = dStart + (key - sStart)
                break
            
    locations.append(key)

print(locations)
print(min(locations))