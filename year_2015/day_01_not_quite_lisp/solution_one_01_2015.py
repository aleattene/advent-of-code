
def find_floor(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    return data.count('(') - data.count(')')
