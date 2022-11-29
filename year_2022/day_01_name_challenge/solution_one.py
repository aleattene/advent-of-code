

def function_name(filename):
    count = 0
    values_list = []

    with open(filename, 'r', encoding='utf-8') as values:
        for value in values:
            values_list.append(int(value.strip("\n")))

    for i in range(len(values_list)-1):
        if values_list[i+1] > values_list[i]:
            count += 1

    return count


# Expected ????
print(function_name('input.txt'))


