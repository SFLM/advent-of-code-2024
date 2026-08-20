def main():
    with open("input.txt") as f:
        raw = f.read().splitlines()
    
    solution1(raw)
    solution2(raw)


def solution1(input):
    input_height = len(input)
    input_width = len(input[0])

    antenna_locations = get_antenna_locations(input)
    antinode_locations = get_antinode_locations(antenna_locations, input_height, input_width)

    print(f"Solution 1: {len(antinode_locations)}")


def solution2(input):
    print()


def get_antenna_locations(input):
    result = {}
    
    for row_no, line in enumerate(input):
        for col_no, symbol in enumerate(line):
            if symbol != '.':
                antenna_position = (row_no, col_no)
                if symbol in result:
                    result[symbol].append(antenna_position)
                else:
                    result[symbol] = [antenna_position]

    return result


def get_antinode_locations(antenna_locations, map_height, map_width):
    antinode_locations = set()

    for frequency in antenna_locations:
        for location in antenna_locations[frequency]:
            for other_location in antenna_locations[frequency]:
                if location == other_location:
                    continue
                row_difference = location[0] - other_location[0]
                column_difference = location[1] - other_location[1]
                antinodes_found = []
                antinodes_found.append((location[0] + row_difference, location[1] + column_difference))
                antinodes_found.append((other_location[0] - row_difference, other_location[1] - column_difference))
                for antinode_location in antinodes_found:
                    if (0 <= antinode_location[0] < map_height) and (0 <= antinode_location[1] < map_width):
                        antinode_locations.add(antinode_location)

    return antinode_locations


if __name__ == "__main__":
    main()