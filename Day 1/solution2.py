
filename = "input.txt"

numTextToDigit = {
    "zero" : "0",
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine": "9"
}


with open(filename) as text:
    res = 0
    for line in text:
        tmp = line
        numbers = []
        spelledNumber = ""
        for c in line:
            if c.isdigit():
                numbers.append(c)
            else:
                spelledNumber += c
                
            if spelledNumber in numTextToDigit:
                numbers.append(numTextToDigit[spelledNumber])
                spelledNumber = c
            else:
                valid = False
                for digit in numTextToDigit:
                    if len(spelledNumber) <= len(digit) and spelledNumber == digit[:len(spelledNumber)]:
                        valid = True

                if not valid:
                    spelledNumber = c
        res += int(numbers[0] + numbers[-1])

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

        numbers2 = []
        for c in line:
            if c.isdigit():
                numbers2.append(c)
        if numbers2 != numbers:
            print("1", numbers)
            print("2", numbers2)
            print(tmp)
            break
            

print(res)