
def get_data_from_file(filename):
    """
    :param filename: str
    :return: str
    """
    with open(filename, 'r', encoding='utf-8') as data:
        return data.read()


def get_start_packet_marker(data, secret_packet):
    """
    :param data: str
    :param secret_packet: int
    :return: int
    """
    position = 0
    valid_sequence = []
    for char in data:
        position += 1
        if char in valid_sequence:
            index = valid_sequence.index(char)
            valid_sequence = valid_sequence[index+1:]
        valid_sequence.append(char)
        if len(valid_sequence) == secret_packet:
            return position


if __name__ == '__main__':
    secret = 4
    print(get_start_packet_marker(get_data_from_file('input.txt'), secret))  # Expected output: 1850


