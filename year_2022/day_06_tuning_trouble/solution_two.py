from solution_one import get_data_from_file, get_start_packet_marker


if __name__ == '__main__':
    secret = 14
    print(get_start_packet_marker(get_data_from_file('input.txt'), secret))  # Expected output: 2823
