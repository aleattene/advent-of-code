
def find_index_position_enter_basement(filename):
    floor = 0
    elevator_map = {
        "(": 1,
        ")": -1
    }

    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()

    for position, symbol in enumerate(data, start=1):
        if symbol in elevator_map:
            floor += elevator_map[symbol]
        if floor < 0:
            return position

