from collections import defaultdict
from utils.file_utils import get_input_file_path, read_input_file


def is_valid_step(x, y, topographic_map, prev_value):
    """Check if the step is within bounds and progresses by +1."""
    return (
        0 <= x < len(topographic_map)
        and 0 <= y < len(topographic_map[0])
        and topographic_map[x][y] == prev_value + 1
    )


def depth_first_search(x, y, topographic_map, path, all_paths, directions, end=9):
    """Perform a depth-first search to find all valid paths."""
    path.append((x, y))
    current_value = topographic_map[x][y]

    # Stop the search if we reach the end value
    if current_value == end:
        all_paths.append(path[:])
        path.pop()
        return

    # Explore all directions recursively
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid_step(new_x, new_y, topographic_map, current_value):
            depth_first_search(new_x, new_y, topographic_map, path, all_paths, directions)

    # Backtrack to explore other paths
    path.pop()


def find_start_positions(topographic_map, start_value=0):
    """Find all starting positions with the given start value."""
    return [
        (i_row, i_col)
        for i_row, row in enumerate(topographic_map)
        for i_col, value in enumerate(row)
        if value == start_value
    ]


def solve_day_10_2024(filename: str) -> tuple[int, int] | str:
    """Find unique paths in a topographic map."""
    try:
        input_file_path = get_input_file_path(__file__, filename)
        data = read_input_file(input_file_path)
    except Exception as error:
        return f"Error: {error}"

    # Parse the input into a 2D grid of integers
    topographic_map = [list(map(int, row)) for row in data]

    # Define the four directions to explore in the grid
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    # Find all start positions and initialize paths
    start_positions = find_start_positions(topographic_map)

    # Perform a depth-first search to find all paths
    all_paths = []
    for x, y in start_positions:
        depth_first_search(x, y, topographic_map, [], all_paths, directions)

    # Find all unique paths by grouping paths by their starting position
    founded = defaultdict(set)
    for path in all_paths:
        start_pos, end_pos = path[0], path[-1]
        founded[start_pos].add(end_pos)

    # Total unique paths (part one) and all discovered paths (part two)
    total_unique_paths = sum(len(end_points) for end_points in founded.values())

    return total_unique_paths, len(all_paths)
