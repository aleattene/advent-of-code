def get_max_calories(filename):
    counter = 0
    max_value = 0
    with open(filename, 'r', encoding='utf-8') as values:
        for value in values:
            if not value.strip("\n"):
                max_value = max(counter, max_value)
                counter = 0
            else:
                counter += int(value.strip("\n"))
    return max_value


# print(get_max_calories('input.txt'))  # Expected output: 71934


