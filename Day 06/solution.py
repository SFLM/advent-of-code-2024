def main():
    with open("input.txt") as f:
        raw = f.read().split()
    
    solution1(raw)
    solution2(raw)


def solution1(input):
    visited_positions = set()
    map_width = len(input[0])
    map_height = len(input)
    guard_row_position, guard_column_position = get_guard_start_position(input)
    obstacle_row_positions = get_obstacle_positions(input)
    obstacle_column_positions = get_obstacle_positions(list(list(zip(*input))))
    heading_index = 0

    while True:
        if heading_index % 2 == 0:  # UP or DOWN
            path, finished = path_to_next_obstacle(guard_row_position, obstacle_column_positions[guard_column_position], heading_index, map_height)
            visited_positions.update([(i, guard_column_position) for i in path])
            if finished:
                break
            guard_row_position = path[-1]
        else:                       # LEFT or RIGHT
            path, finished = path_to_next_obstacle(guard_column_position, obstacle_row_positions[guard_row_position], heading_index, map_width)
            visited_positions.update([(guard_row_position, i) for i in path])
            if finished:
                break
            guard_column_position = path[-1]
        
        heading_index = (heading_index + 1) % 4

    # draw(input, visited_positions)
    print(f"Solution 1: {len(visited_positions)}")


def solution2(input):
    loops = 0
    map_width = len(input[0])
    map_height = len(input)
    guard_row_position, guard_column_position = get_guard_start_position(input)
    obstacle_row_positions = get_obstacle_positions(input)
    obstacle_column_positions = get_obstacle_positions(list(list(zip(*input))))

    new_obstacle_positions = []

    for row_no in range(map_height):
        for col_no in range(map_width):
            if (row_no not in obstacle_row_positions) or (col_no not in obstacle_row_positions[row_no]):
                new_obstacle_positions.append((row_no, col_no))

    for new_obstacle_position in new_obstacle_positions:
        if has_loop(guard_row_position, guard_column_position, obstacle_row_positions, obstacle_column_positions, new_obstacle_position, 0, map_width, map_height, set()):
            loops += 1

    print(f"Solution 2: {loops}")


def has_loop(row_pos, col_pos, obstacle_row_positions, obstacle_column_positions, new_obstacle_position, heading, map_width, map_height, endings):
    if (row_pos, col_pos, heading) in endings: # Loop found
        return True
    if row_pos in obstacle_row_positions:
        if (col_pos in obstacle_row_positions[row_pos]) or ((row_pos, col_pos) == new_obstacle_position): # Starting inside an obstacle
            return False
    endings.add((row_pos, col_pos, heading))

    if heading % 2 == 0:        # UP or DOWN
        if col_pos not in obstacle_column_positions:
            return False
        if col_pos == new_obstacle_position[1]:
            obstacle_list = sorted(obstacle_column_positions[col_pos] + [new_obstacle_position[0]])
        else:
            obstacle_list = obstacle_column_positions[col_pos]
        path, escaped = path_to_next_obstacle(row_pos, obstacle_list, heading, map_height)

        if escaped:
            return False
        row_pos = path[-1]
    else:                       # LEFT or RIGHT
        if row_pos not in obstacle_row_positions:
            return False
        if row_pos == new_obstacle_position[0]:
            obstacle_list = sorted(obstacle_row_positions[row_pos] + [new_obstacle_position[1]])
        else:
            obstacle_list = obstacle_row_positions[row_pos]
        path, escaped = path_to_next_obstacle(col_pos, obstacle_list, heading, map_width)

        if escaped:
            return False
        col_pos = path[-1]
        
    return has_loop(row_pos, col_pos, obstacle_row_positions, obstacle_column_positions, new_obstacle_position, (heading + 1) % 4, map_width, map_height, endings)


def draw(map, positions):
    for line_no, line in enumerate(map):
        for col_no, sym in enumerate(line):
            if (line_no, col_no) in positions:
                print('X', end='')
            else:
                print(sym, end='')
        print()


def path_to_next_obstacle(guard_position, obstacle_list, direction, max):
    if direction in (0, 3):  # LEFT or UP
        next_obstacle = next((position for position in reversed(obstacle_list) if position < guard_position), None)
        if next_obstacle == None:
            return list(range(guard_position, -1, -1)), True
        return list(range(guard_position, next_obstacle, -1)), False
    else:               # RIGHT or DOWN
        next_obstacle = next((position for position in obstacle_list if position > guard_position), None)
        if next_obstacle == None:
            return list(range(guard_position, max, 1)), True
        return list(range(guard_position, next_obstacle, 1)), False


def get_guard_start_position(map):
    for row_no, line in enumerate(map):
        for col_no, symbol in enumerate(line):
            if symbol == '^':
                return row_no, col_no
    return (-1, -1)


def get_obstacle_positions(map):
    obstacle_positions = {}
    for row_no, line in enumerate(map):
        for column_no, symbol in enumerate(line):
            if symbol == '#':
                if row_no in obstacle_positions:
                    obstacle_positions[row_no].append(column_no)
                else:
                    obstacle_positions[row_no] = [column_no]
    return obstacle_positions


if __name__ == "__main__":
    main()