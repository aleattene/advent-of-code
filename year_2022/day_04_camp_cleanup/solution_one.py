

def get_data_from_file(filename):
    """
    :param filename: str
    :return: list
    """
    import re
    with open(filename, 'r', encoding='utf-8') as data:
        return[list(map(int, re.findall('[0-9]+', sections))) for sections in data.read().split('\n')]


def get_overlapping_sections(data):
    """
    :param data: list
    :return: int
    """
    return sum([1 for pos in data if (pos[0] >= pos[2] and pos[1] <= pos[3]) or (pos[2] >= pos[0] and pos[3] <= pos[1])])


if __name__ == '__main__':
    print(get_overlapping_sections(get_data_from_file('input.txt')))  # Expected output: 595


