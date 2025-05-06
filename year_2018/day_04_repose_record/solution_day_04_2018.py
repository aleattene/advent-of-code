from collections import defaultdict, Counter
from utils.file_utils import get_input_file_path, read_input_file


def solve_day_04_2018(filename: str) -> tuple[int, int]:
    """
    Solution of the Advent of Code 2018 Day 04 - Repose Record.
    :param filename: The name of the input file containing the room data.
    :return: A tuple containing the results for part 1 and part 2 of the challenge.
    """
    try:
        # Create the absolute path of the input file
        input_file_path = get_input_file_path(__file__, filename)
        # Read the input file
        data = sorted(read_input_file(input_file_path))
    except Exception as error:
        raise RuntimeError(f"Error: {error}")

    # Dictionary to store for each guard the minutes they slept and how many times ( guard_id: { minute: count} )
    guards_minute_counts = defaultdict(Counter)

    active_guard = None
    sleep_start = None

    # Process each log entry (example: [1518-11-01 00:00] Guard #10 begins shift)
    for log in data:
        # Extract the date, time, guard ID, and event from the log entry
        log_datetime, event = log.split("] ", 1)
        minute_event = int(log_datetime[-2:])
        instructions = event.split(" ")

        # Check if the log entry is for a guard shift, falls asleep, or wakes up
        if instructions[0] == "Guard":
            active_guard = instructions[1][1:]
        elif instructions[0] == "falls":
            sleep_start = minute_event
        else:
            # If the guard wakes up, update the sleep time for the active guard
            minutes = list(range(sleep_start, minute_event))
            guards_minute_counts[active_guard].update(minutes)

    # Find the guard who slept the most
    guard_most_minutes_sleep = max(
        guards_minute_counts,
        key=lambda guard_id: sum(guards_minute_counts[guard_id].values())
    )

    # Find the minute when the found guard slept the most
    minute_most_sleep = max(
        guards_minute_counts[guard_most_minutes_sleep].keys(),
        key=lambda minute: guards_minute_counts[guard_most_minutes_sleep][minute]
    )

    # Return the product of the guard ID who slept the most and the minute they slept the most (part 1)
    result_1 = int(guard_most_minutes_sleep) * minute_most_sleep

    # Initialize variable for part 2 (start with the same guard and minute as part 1)
    minute_most_sleep_count = guards_minute_counts[guard_most_minutes_sleep][minute_most_sleep]

    # Find the guard who slept the most on the same minute
    for guard, counts in guards_minute_counts.items():
        # Find the minute with the highest sleep count for each guard
        minute_sleep, minute_count = counts.most_common(1)[0]
        # Check if this guard has the highest sleep count on the same minute and update the variables if necessary
        if minute_count > minute_most_sleep_count:
            minute_most_sleep_count, guard_most_minutes_sleep, minute_most_sleep = minute_count, guard, minute_sleep

    # Return the product of the guard ID who slept the most on the same minute and that minute (part 2)
    result_2 = int(guard_most_minutes_sleep) * minute_most_sleep

    return result_1, result_2


if __name__ == "__main__":

    # Import function to print results
    import time
    from utils.file_utils import print_day_results

    # Calculate results for demo and real input files
    demo_1, demo_2 = solve_day_04_2018("input_demo.txt")
    start_time = time.time()
    solution_1, solution_2 = solve_day_04_2018("input.txt")
    end_time = time.time()

    # Calculate execution time in milliseconds
    execution_time = int((end_time - start_time) * 1000)

    # Print results in a formatted table (using rich)
    print_day_results(
        "2018", "04",
        str(demo_1), str(demo_2),
        str(solution_1), str(solution_2),
        execution_time
    )
