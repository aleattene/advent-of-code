
def solve_day_02_2015_one(filename: str) -> int | str:
    try:
        square = 0
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.read()
            for line in data.split("\n"):
                dimensions = line.split("x")
                l, w, h = int(dimensions[0]), int(dimensions[1]), int(dimensions[2])
                sides = [l*w, w*h, h*l]
                square += 2*sum(sides) + min(sides)
        return square
    except Exception as error:
        return f"Error: {error}"
