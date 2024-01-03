import numpy as np

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


(feed,) = [name for name, module in modules.items() if "rx" in module["dst"]]
cycleLengths = {}
numFeedInputs = sum(1 for name, module in modules.items() if feed in module["dst"])
presses = 0

while True:
    events = [("button", False, "broadcaster")] # (src, pulse type, dest)
    presses += 1
    while events:

        src, pulse, dest = events.pop(0)

        #print(src, "-", pulse, "-> ", dest)

        if dest == feed and pulse:
            if src not in cycleLengths:
                cycleLengths[src] = presses

            if len(cycleLengths) == numFeedInputs:
                print(cycleLengths)
                print(np.lcm.reduce(list(cycleLengths.values())))
                exit()

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
