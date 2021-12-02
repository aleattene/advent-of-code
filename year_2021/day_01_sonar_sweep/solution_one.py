

def count_increments(filename):
    values_list = []
    count = 0

    with open(filename, 'r', encoding='utf-8') as values:
        for value in values:
            values_list.append(int(value.strip("\n")))

    for i in range(len(values_list)-1):
        if values_list[i+1] > values_list[i]:
            count += 1

    return count


# Expected 1655
print(count_increments('input.txt'))


