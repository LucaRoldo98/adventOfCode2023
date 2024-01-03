
filename = "input.txt"

with open(filename) as text:
    res = 0
    for line in text:
        line = line.replace("zero", "zer0ero")
        line = line.replace("one", "on1ne")
        line = line.replace("two", "tw2wo")
        line = line.replace("three", "thre3hree")
        line = line.replace("four", "fou4our")
        line = line.replace("five", "fiv5ive")
        line = line.replace("six", "si6ix")
        line = line.replace("seven", "seve7even")
        line = line.replace("eight", "eigh8ight")
        line = line.replace("nine", "nin9ine")

        numbers = []
        for c in line:
            if c.isdigit():
                numbers.append(c)
        res += int(numbers[0] + numbers[-1])

print(res)