

def lantern_fish(filename, days):

    # Data structure that will contain occurrences of fish
    occurrences = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Retrieval of data from the input file
    with open(filename, 'r', encoding='utf-8') as values:
        for value in values:
            fish_list = value.split(",")

    # Data entry into the data structure of occurrences of fish
    for fish in fish_list:
        occurrences[int(fish)] += 1

    # Solution algorithm
    for day in range(1, days+1):
        tmp = occurrences[0]
        for i in range(0, len(occurrences)-1):
            occurrences[i] = occurrences[i+1]
        occurrences[8] = tmp
        occurrences[6] += tmp

    # Returns the number of fish
    return sum(occurrences)
