
def get_score(filename):
    scores = {
        'AX': 4, 'AY': 8, 'AZ': 3,
        'BY': 5, 'BZ': 9, 'BX': 1,
        'CZ': 6, 'CX': 7, 'CY': 2
    }
    total_score = 0
    with open(filename, 'r', encoding='utf-8') as rounds:
        for match in rounds:
            total_score += scores[match.strip('\n')[0:3:2]]
    return total_score


# print(get_score('input.txt'))  # Expected output: 13009


