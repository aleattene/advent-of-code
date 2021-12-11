

def find_entries_2020(filename):
    values_list = []
    with open(filename, 'r', encoding='utf-8') as values:
        for value in values:
            values_list.append(int(value.strip("\n")))
    for i in range(len(values_list)- 2):
        for j in range(1, len(values_list)-1):
            for k in range(2, len(values_list)):
                if values_list[i] + values_list[j] + values_list[k] == 2020:
                    return values_list[i]*values_list[j]*values_list[k]
