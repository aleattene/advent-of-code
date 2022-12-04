from solution_one import get_data_from_file


def get_overlapping_sections(data):
    """
    :param data: list
    :return: int
    """
    return sum([1 for pos in data if pos[2] <= pos[0] <= pos[3] or pos[2] <= pos[1] <= pos[3] or
                                     pos[0] <= pos[2] <= pos[1] or pos[0] <= pos[3] <= pos[1]])


if __name__ == '__main__':
    print(get_overlapping_sections(get_data_from_file('input.txt')))  # Expected output: 952
