filename = "input.txt"

sequence = []

with open(filename) as text:
    for i,row in enumerate(text):
        sequence = row.split(",")

def hash(cmd):
    curr = 0
    for ch in cmd:
        curr += ord(ch)    
        curr *= 17
        curr %= 256
    return curr

res = 0

for cmd in sequence:
    cmdHash = hash(cmd)
    print(cmdHash)
    res += cmdHash

print(res)

    