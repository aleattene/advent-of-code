

def get_data_from_file(filename):
    """
    :param filename: str
    :return: data: list
    """
    import re
    with open(filename, 'r', encoding='utf-8') as data:
        return [re.findall('[0-9]+', p) for p in data.read().split('\n')]


def get_overlapping_sections(data):
    """
    :param data: list
    :return: int
    """
    return sum([1 for pair in data if (int(pair[0]) >= int(pair[2]) and int(pair[1]) <= int(pair[3])) or
                int(pair[2]) >= int(pair[0]) and int(pair[3]) <= int(pair[1])])


if __name__ == '__main__':
    print(get_overlapping_sections(get_data_from_file('input.txt')))  # Expected output: 595


