from math import gcd


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
    input_height = len(input)
    input_width = len(input[0])

    antenna_locations = get_antenna_locations(input)
    antinode_locations = get_antinode_locations(antenna_locations, input_height, input_width, resonant_harmonics=True)

    print(f"Solution 2: {len(antinode_locations)}")


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


def get_antinode_locations(antenna_locations, map_height, map_width, resonant_harmonics=False):
    antinode_locations = set()

    for frequency in antenna_locations:
        for location in antenna_locations[frequency]:
            for other_location in antenna_locations[frequency]:
                if location == other_location:
                    continue
                difference = (location[0] - other_location[0], location[1] - other_location[1])

                if resonant_harmonics:
                    greatest_common_denominator = gcd(difference[0], difference[1])
                    difference = (difference[0] // greatest_common_denominator, difference[1] // greatest_common_denominator)
                    if len(antenna_locations[frequency]) > 1:
                        antinode_locations.update([location, other_location])

                current_location = location
                while True:
                    antinode_found = find_antinode(current_location, difference, False)
                    if (0 <= antinode_found[0] < map_height) and (0 <= antinode_found[1] < map_width):
                        antinode_locations.add(antinode_found)
                        if not resonant_harmonics:
                            break
                        current_location = antinode_found
                    else:
                        break
                if not resonant_harmonics:
                    antinode_found = find_antinode(other_location, difference, True)
                    if (0 <= antinode_found[0] < map_height) and (0 <= antinode_found[1] < map_width):
                        antinode_locations.add(antinode_found)

    return antinode_locations


def find_antinode(anchor, difference, far_end):
    if far_end:
        return (anchor[0] - difference[0], anchor[1] - difference[1])
    return (anchor[0] + difference[0], anchor[1] + difference[1])


if __name__ == "__main__":
    main()