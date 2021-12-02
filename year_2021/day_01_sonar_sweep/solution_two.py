

def count_increments(filename):
    values_list = []
    count = 0

    with open(filename, 'r', encoding='utf-8') as values:
        for value in values:
            values_list.append(int(value.strip("\n")))

    for i in range(len(values_list)-1):
        if sum(values_list[i+1:i+4]) > sum(values_list[i:i+3]):
            count += 1

    return count


# Expected 1683
print(count_increments('input.txt'))
