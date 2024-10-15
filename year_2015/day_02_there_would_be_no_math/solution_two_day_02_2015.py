
def solve_day_02_2015_two(filename: str) -> int | str:
    try:
        total_ribbon = 0
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                l, w, h = map(int, line.split("x"))
                ribbon_bow = l*w*h
                ribbon_feet = 2*sum(sorted([l, w, h])[:2]) + ribbon_bow
                total_ribbon += ribbon_feet
        return total_ribbon
    except Exception as error:
        return f"Error: {error}"
