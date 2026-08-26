from collections import deque, defaultdict


def main():
    with open("input.txt") as f:
        raw = f.read()
    
    solution1(raw)
    solution2(raw)


def solution1(disk_map: str):
    print(f"Solution 1: {calculate_checksum(tidy(unzip(disk_map)))}")


def solution2(disk_map: str):
    print(f"Solution 2: {calculate_checksum(tidy_advanced(*separate(disk_map)))}")


def separate(disk_map: str):
    files, spaces = [list(map(int, list(tup))) for tup in zip(*zip(disk_map[::2], disk_map[1::2]))]
    files.append(int(disk_map[-1]))
    return (deque(files), spaces)


def unzip(disk_map: str):
    result = deque()
    file_id = 0
    for block_no, block in enumerate(disk_map):
        symbol = '.'
        if block_no % 2 == 0:
            symbol = file_id
            file_id += 1
        [result.append(symbol) for _ in range(int(block))]
    return result


def tidy(unzipped_file: deque):
    result = deque()
    while len(unzipped_file) > 0:
        current_left = unzipped_file.popleft()
        if current_left == '.':
            while len(unzipped_file) > 0:
                current_right = unzipped_file.pop()
                if current_right != '.':
                    result.append(current_right)
                    break
        else:
            result.append(current_left)
    return result


def tidy_advanced(files: deque, spaces: list):
    result = deque()
    file_id = len(files)-1
    moved_items = defaultdict(list)
    while len(spaces)>0:
        file_volume = files.pop()
        for space_index, space in enumerate(spaces):
            if file_volume<=space:
                spaces[space_index]-=file_volume
                moved_items[space_index].extend([*[file_id]*file_volume])
                addition = [*moved_items[len(spaces)-1], *['.']*spaces.pop(), *['.']*file_volume]
                break
        else:
            addition = [*moved_items[len(spaces)-1], *['.']*spaces.pop(), *[file_id]*file_volume]
        result.extendleft(reversed(addition))
        file_id-=1
    result.extendleft([*['0']*files[0]])

    return result


def calculate_checksum(tidy_file: deque):
    result = 0
    step = 0
    while len(tidy_file)>0:
        current = tidy_file.popleft()
        if current != '.':
            result += int(current)*step
        step+=1
    return result


if __name__ == "__main__":
    main()