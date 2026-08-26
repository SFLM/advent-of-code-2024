def main():
    with open("input.txt") as f:
        raw = f.read().splitlines()
    
    solution1(raw)
    solution2(raw)


def solution1(input):
    result = 0
    topographic_map = [tuple([int(height) for height in line]) for line in input]
    for trailhead_location in get_trailheads(topographic_map):
        trailhead_row, trailhead_column = trailhead_location
        trailhead_set = trailhead_solver(topographic_map, trailhead_row, trailhead_column, set())
        if trailhead_set != None:
            result += len(trailhead_set)
    print(f"Solution 1: {result}")


def solution2(topographic_map):
    print()


def get_trailheads(topographic_map):
    trailheads = []
    for row, line in enumerate(topographic_map):
        for column, height in enumerate(line):
            if height == 0:
                trailheads.append((row,column))
    return trailheads


def trailhead_solver(topographic_map, row, column, found, last_value=-1):
    if row<0 or row>=len(topographic_map) or column<0 or column>=len(topographic_map[0]):
        return
    
    value = topographic_map[row][column]

    if value != last_value+1:
        return
    if value == 9:
        found.add((row,column))
        return
    
    trailhead_solver(topographic_map, row, column-1, found, value)
    trailhead_solver(topographic_map, row, column+1, found, value)
    trailhead_solver(topographic_map, row+1, column, found, value)
    trailhead_solver(topographic_map, row-1, column, found, value)

    return found


if __name__ == "__main__":
    main()