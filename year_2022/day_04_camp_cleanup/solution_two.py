from solution_one import get_data_from_file


def get_overlapping_sections(data):
    """
    :param data: list
    :return: int
    """
    return sum([1 for pair in data if int(pair[2]) <= int(pair[0]) <= int(pair[3]) or
                int(pair[2]) <= int(pair[1]) <= int(pair[3]) or
                int(pair[0]) <= int(pair[2]) <= int(pair[1]) or
                int(pair[0]) <= int(pair[3]) <= int(pair[1])])


if __name__ == '__main__':
    print(get_overlapping_sections(get_data_from_file('input.txt')))  # Expected output: 952
