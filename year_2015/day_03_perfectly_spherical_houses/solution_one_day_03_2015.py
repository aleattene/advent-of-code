
def solve_day_03_2015_one(filename: str) -> int | str:
    try:
        # Initial position
        x, y = 0, 0
        # Set of Visited houses
        visited = {(x, y)}
        with open(filename, 'r', encoding='utf-8') as f:
            for direction in f.read():
                match direction:
                    case "^": y += 1
                    case "v": y -= 1
                    case ">": x += 1
                    case "<": x -= 1
                visited.add((x, y))
        return len(visited)
    except Exception as error:
        return f"Error: {error}"
