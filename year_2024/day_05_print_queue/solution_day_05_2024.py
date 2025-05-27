from utils.file_utils import get_input_file_path, read_input_file
from collections import defaultdict


def create_dict_from_pair_rules(rules: list[str]) -> dict[int, set[int]]:
    """Create a dictionary from a list of rules, from 'num1|num2' to {'num1': {'num2', ...}}."""
    result_dict: dict[int, set[int]] = defaultdict(set)

    for rule in rules:
        prev_page, next_page = rule.split('|')
        result_dict[int(prev_page)].add(int(next_page))

    return result_dict


def verify_sequence(sequence: list[int], num_dict: dict[int, set[int]]) -> tuple[bool, int]:
    """Verify if each number in the sequence is present in the dictionary of tuples."""
    for i in range(len(sequence) - 1):
        current_num: int = sequence[i]
        next_num: int = sequence[i + 1]

        # Check if the current number is a key present in the dictionary
        if next_num not in num_dict.get(current_num, set()):
            return False, 0

    # If the sequence is valid, return True and the middle number of the sequence
    return True, sequence[len(sequence) // 2]


def reorder_sequence(sequence: list[int], num_dict: dict[int, set[int]]) -> list[int]:
    """Reorder a sequence to make it compliant with the dictionary rules."""
    is_sequence_stable: bool = False

    # Iterate until the sequence is stable
    while not is_sequence_stable:
        is_sequence_stable: bool = True
        for i in range(len(sequence) - 1):
            current_num: int = sequence[i]
            next_num: int = sequence[i + 1]

            # If the next number is not in the tuple of the current number, swap the elements
            if next_num not in num_dict.get(current_num, set()):
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
                is_sequence_stable: bool = False

    return sequence


def solve_day_05_2024(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2024 Day 05 - Print Queue.
    :param filename: The name file containing the input data.
    :return: A tuple containing the total_1 of middle numbers from valid sequences (solution 1)
                and the total_1 of middle numbers from reordered valid sequences (solution 2).
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = read_input_file(input_file_path)
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Create the dictionary of ordering rules and the list of updating rules
    idx_end_ordering_rules: int = data.index("")
    ordering_rules: dict[int, set[int]] = create_dict_from_pair_rules(data[:idx_end_ordering_rules])
    updating_rules: list[str] = data[idx_end_ordering_rules + 1:]

    # Initialize the counters
    total_1: int = 0
    total_2: int = 0
    for update_rule in updating_rules:
        # Convert the update rule into a list of integers
        elements_rules: list[int] = list(map(int, update_rule.split(",")))
        # Verify the sequence against the ordering rules
        result: tuple[bool, int] = verify_sequence(elements_rules, ordering_rules)
        # If the sequence is valid, add the middle number to the total_1 (part 1)
        if result[0]:
            total_1 += result[1]
        else:
            # If the sequence is not valid, reorder it and verify it again (part 2)
            reordered_sequence: list[int] = reorder_sequence(elements_rules, ordering_rules)
            is_valid, mid_value = verify_sequence(reordered_sequence, ordering_rules)
            if is_valid:
                total_2 += mid_value

    return total_1, total_2


if __name__ == "__main__":
    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_05_2024("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_05_2024("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time: int = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2024", "05",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )