
def solve_day_03_2015_two(filename: str) -> int | str:
    try:
        # Initial position
        x, y = 0, 0
        # Initial position of Santa
        x_santa, y_santa = 0, 0
        # Initial position of Robo-Santa
        x_robo, y_robo = 0, 0
        # Set of Visited houses
        visited = {(x, y)}
        with open(filename, 'r', encoding='utf-8') as f:
            for i, direction in enumerate(f.read()):
                # Santa moves on even steps
                if i % 2 == 0:
                    match direction:
                        case "^": y_santa += 1
                        case "v": y_santa -= 1
                        case ">": x_santa += 1
                        case "<": x_santa -= 1
                    visited.add((x_santa, y_santa))
                # Robo-Santa moves on odd steps
                else:
                    match direction:
                        case "^": y_robo += 1
                        case "v": y_robo -= 1
                        case ">": x_robo += 1
                        case "<": x_robo -= 1
                    visited.add((x_robo, y_robo))
        return len(visited)
    # Handle generic exceptions
    except Exception as error:
        return f"Error: {error}"


