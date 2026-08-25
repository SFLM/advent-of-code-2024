from collections import deque


def main():
    with open("input.txt") as f:
        raw = f.read()
    
    solution1(raw)
    solution2(raw)


def solution1(disk_map):
    print(f"Solution 1: {calculate_checksum(tidy(unzip(disk_map)))}")


def solution2(input):
    print()


def separate(disk_map):
    list1, list2 = [list(tup) for tup in zip(*zip(disk_map[::2], disk_map[1::2]))]
    list1.append(disk_map[-1])
    for h in list1:
        print(h, end='')
    print()
    for h in list2:
        print(h, end='')


def unzip(disk_map):
    result = deque()
    file_id = 0
    for block_no, block in enumerate(disk_map):
        symbol = '.'
        if block_no % 2 == 0:
            symbol = file_id
            file_id += 1
        # [print(symbol, end='') for _ in range(int(block))]
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


def calculate_checksum(tidy_file: deque):
    result = 0
    file_id = 0
    while len(tidy_file) > 0:
        result += file_id * tidy_file.popleft()
        file_id += 1
    return result


if __name__ == "__main__":
    main()