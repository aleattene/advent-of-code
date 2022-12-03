from solution_one import get_data_from_file, from_ascii_to_priority


def get_priority_rucksacks_groups(data):
    """
    :param data: list
    :return: total_priority: int
    """
    total_priority = 0
    groups = []
    for rucksack in data:
        groups.append(rucksack.strip('\n'))
        if len(groups) == 3:
            for letter in groups[0]:
                if letter in groups[1] and letter in groups[2]:
                    total_priority += from_ascii_to_priority(letter)
                    break
            groups = []
    return total_priority


if __name__ == '__main__':
    print(get_priority_rucksacks_groups(get_data_from_file('input.txt')))  # Expected output: 2881
