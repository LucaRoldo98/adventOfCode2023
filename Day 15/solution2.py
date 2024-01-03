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


boxes = [{} for _ in range(256)]

for cmd in sequence:
    separator = "=" if "=" in cmd else "-" 
    lens = cmd.split(separator)[0]
    lensHash = hash(lens)
    if separator == "-" and lens in boxes[lensHash]:
        del boxes[lensHash][lens]
    
    if separator == "=":
        focalLength = int(cmd.split(separator)[1])
        if lens in boxes[lensHash]: boxes[lensHash][lens] = focalLength
        else: boxes[lensHash][lens] = focalLength

res = 0

for i,box in enumerate(boxes):
    for j,lens in enumerate(box):
        focusPwr = (i+1) * (j+1) * box[lens]
        print(focusPwr)
        res += focusPwr

print(res)

    