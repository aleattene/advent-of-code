def from_file_to_data(filename):
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


# print(from_file_to_data('input.txt'))  # Expected output: 71934


