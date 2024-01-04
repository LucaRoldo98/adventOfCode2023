filename = "input.txt"

possibleGames = []
constraint = {
    "red" : 12,
    "green": 13,
    "blue" : 14
}

# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

with open(filename) as text:

    for row in text:
        row = row.split(":") 
        gameID = int(row[0].split(" ")[-1])
        picks = row[1].split(";")
        possible = True
        for pick in picks:
            colors = pick.split(",")
            for color in colors:
                color = color.replace("\n", "").strip().split(" ")
                if int(color[0]) > constraint[color[1]]:
                    possible = False
                    break
            if not possible: break
        
        if possible:
            possibleGames.append(gameID)
    
print(possibleGames)
print(sum(possibleGames))