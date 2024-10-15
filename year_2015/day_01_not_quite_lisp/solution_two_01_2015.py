
def find_index_position_enter_basement(filename):
    elevator_map = {
        "(": 1,
        ")": -1
    }
    floor = 0
    position = 0

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for symbol in line:
                position += 1
                if symbol in elevator_map:
                    floor += elevator_map[symbol]
                if floor < 0:
                    return position

