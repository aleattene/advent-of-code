def get_sum_max_three_calories(filename):
    counter = 0
    max_values = [0, 0, 0]
    with open(filename, 'r', encoding='utf-8') as calories:
        for cal in calories:
            if not cal.strip("\n"):
                max_values.sort()
                max_values[0] = max(counter, max_values[0])
                counter = 0
            else:
                counter += int(cal.strip("\n"))
    return sum(max_values)


# print(get_sum_max_three_calories('input.txt'))  # Expected output: 211447
