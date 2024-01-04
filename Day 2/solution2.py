filename = "input.txt"

# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

gamePowers = []

with open(filename) as text:

    for row in text:
        row = row.split(":") 
        gameID = int(row[0].split(" ")[-1])
        picks = row[1].split(";")
        minCubes = {
            "red" : 0,
            "blue": 0,
            "green" : 0
        }
        for pick in picks:
            colors = pick.split(",")
            for color in colors:
                color = color.replace("\n", "").strip().split(" ")
                minCubes[color[1]] = max(int(color[0]), minCubes[color[1]])
        
        gamePowers.append(minCubes["red"] * minCubes["blue"] * minCubes["green"])

    
print(gamePowers)
print(sum(gamePowers))