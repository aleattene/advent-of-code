

def get_data_from_file(filename):
    """
    :param filename: str
    :return: data: list
    """
    with open(filename, 'r', encoding='utf-8') as data:
        return data.read().split('\n')


def from_ascii_to_priority(letter):
    """
    :param letter: str
    :return: int
    """
    return ord(letter) - 96 if 97 <= ord(letter) <= 122 else ord(letter) - 38


def get_priority_rucksacks(data):
    """
    :param data: list
    :return: total_priority: int
    """
    total_priority = 0
    for rucksack in data:
        divisor = len(rucksack) // 2
        for letter in rucksack[:divisor]:
            if letter in rucksack[divisor:]:
                total_priority += from_ascii_to_priority(letter)
                break
    return total_priority


if __name__ == '__main__':
    print(get_priority_rucksacks(get_data_from_file('input.txt')))  # Expected output: 7980


