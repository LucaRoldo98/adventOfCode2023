def get_numerical_digit(word):
    numerical_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    return numerical_dict.get(word.lower(), '')

def process_line(line):
    # Remove non-alphanumeric characters and split the line into words
    words = ''.join(c for c in line if c.isalnum() or c.isspace()).split()

    # Get the real first and last digits, convert them to numerical form
    first_digit = get_numerical_digit(words[0])
    last_digit = get_numerical_digit(words[-1])

    return int(first_digit + last_digit)

def main(filename):
    total_sum = 0

    with open(filename, 'r') as file:
        for line in file:
            total_sum += process_line(line)

    print(f"Total Sum: {total_sum}")

if __name__ == "__main__":
    filename = "test.txt"  # Replace with the actual path to your input file
    main(filename)
