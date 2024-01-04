
filename = "input.txt"

with open(filename) as text:
    res = 0
    for line in text:
        numbers = []
        for c in line:
            if c.isdigit():
                numbers.append(c)
        res += int(numbers[0] + numbers[-1])

print(res)