from utils.file_utils import get_input_file_path, read_input_file


def solve_day_01_2017(filename: str) -> tuple[int, int] | str:
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)[0]
    except Exception as error:
        return f"Error: {error}"

    # Calculate and return the captcha sums for both parts (circular and half-circular sequences)
    captcha_sum_1 = sum(int(data[position_digit])
                        for position_digit in range(len(data))
                        if data[position_digit] == data[position_digit - 1])
    captcha_sum_2 = sum(int(data[position_digit]) * 2
                        for position_digit in range(len(data)//2)
                        if data[position_digit] == data[position_digit + len(data)//2])

    return captcha_sum_1, captcha_sum_2

