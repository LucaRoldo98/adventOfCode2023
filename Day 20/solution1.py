filename = "input.txt"

modules = {} # "id" : {"type", "destinations", "state" , "remember" : [low], } 

with open(filename) as text:
    for i,row in enumerate(text):
        o, d = row.split(" -> ")
        type = o[0]
        id = o if o == "broadcaster" else o[1:]
        modules[id] = {
            "type" : type,
            "dst" : d.strip().split(", "),
            "s" : False,
            "pls" : {} }

for m in modules:
    if modules[m]["type"] == "&":
        for m2 in modules:
            if m in modules[m2]["dst"]:
                modules[m]["pls"][m2] = False


lows = 0
highs = 0

for cycleNum in range(1000): 
    events = [("button", False, "broadcaster")] # (src, pulse type, dest)
    while events:

        src, pulse, dest = events.pop(0)

        #print(src, "-", pulse, "-> ", dest)

        if pulse: highs += 1
        else: lows += 1

        if dest not in modules: continue

        if dest == "broadcaster":
            newPulse = pulse

        elif modules[dest]["type"] == "%":
            if pulse: continue
            else: 
                newPulse = modules[dest]["s"] = not modules[dest]["s"]
        
        elif modules[dest]["type"] == "&":
            modules[dest]["pls"][src] = pulse
            newPulse = sum(modules[dest]["pls"].values()) != len(modules[dest]["pls"])

        for d in modules[dest]["dst"]:
            events.append((dest, newPulse, d))

print(lows * highs)