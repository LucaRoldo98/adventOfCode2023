filename = "input.txt"

workflows = {}
parts = []

readingWorkflows = True

def parseWorkflows(workflow):
    id, instructions = workflow.strip().split("{")
    instructions = "".join(filter(lambda x: x != "{" and x != "}", instructions))
    return id, instructions.split(",")

def parseParts(part):
    parsedParts = {}
    part = "".join(filter(lambda x: x != "{" and x != "}", part))
    for category in part.split(","):
        id, val = category.split("=")
        parsedParts[id] = int(val)
    return parsedParts

with open(filename) as text:
    for i,row in enumerate(text):
        if row == "\n":
            readingWorkflows = False

        elif readingWorkflows:
            id, rules = parseWorkflows(row)
            workflows[id] = rules
        
        else:
            parts.append(parseParts(row))

A = []

for part in parts:
    currFlow = "in"
    while True:

        if currFlow == "A":
            A.append(part)
            break
        if currFlow == "R":
            break

        for rule in workflows[currFlow]:
            divider = ">" if ">" in rule else "<" if "<" in rule else None
            if not divider: # Default case
                currFlow = rule
                break
            rule, destination = rule.split(":")
            cat, val = rule.split(divider)
            val = int(val)

            if (divider == ">" and part[cat] > val) or (divider == "<" and part[cat] < val):
                currFlow = destination
                break

res = 0

for el in A:
    res += sum(list(el.values()))

print(res)

