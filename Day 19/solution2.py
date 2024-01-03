filename = "input.txt"

workflows = {}


def parseWorkflows(workflow):
    id, instructions = workflow.strip().split("{")
    instructions = "".join(filter(lambda x: x != "{" and x != "}", instructions))
    return id, instructions.split(",")


with open(filename) as text:
    for i,row in enumerate(text):
        if row == "\n":
            break

        id, rules = parseWorkflows(row)
        workflows[id] = rules

A = []

parts = [("in", {"x" : (1,4000), "m": (1,4000), "a": (1,4000), "s": (1,4000)})]

while parts:
    currFlow, partRange = parts.pop(0)
    if currFlow == "A":
        A.append(partRange)
        continue
    if currFlow == "R":
        continue

    currObj = partRange
    for rule in workflows[currFlow]:
        divider = ">" if ">" in rule else "<" if "<" in rule else None
        if not divider: # Default case
            parts.append((rule, currObj))
            break
        rule, destination = rule.split(":")
        cat, val = rule.split(divider)
        val = int(val)

        if divider == ">" and currObj[cat][1] > val:
            newObj = currObj.copy()
            newObj[cat] = (val+1, currObj[cat][1])
            currObj[cat] = (currObj[cat][0], val)
            parts.append((destination, newObj))
        
        elif divider == "<" and currObj[cat][0] < val:
            newObj = currObj.copy()
            newObj[cat] = (currObj[cat][0], val-1)
            currObj[cat] = (val, currObj[cat][1])
            parts.append((destination, newObj))

res = 0

for obj in A:
    combinations = 1
    for cat in obj:
        combinations *= (obj[cat][1] + 1 - obj[cat][0])
    res += combinations

print(res)

