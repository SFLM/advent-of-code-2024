from collections import deque

def main():
    with open("example2.txt") as f:
        raw = f.read().split()
    
    solution1(raw)

def solution1(input):
    find_xmas(input)

def solution2(input):
    print()

def find_xmas(input_map):
    total = 0

    total += find_xmas_straight(input_map) # Horizontal
    total += find_xmas_straight(zip(*input_map[::-1])) # Vertical
    # TODO: Diagonals

    print(total)

def find_xmas_straight(input_map):
    total = 0
    for row in input_map:
        horizontal_window = deque(['.','.','.','.'])
        for letter in row:
            horizontal_window.popleft()
            horizontal_window.append(letter)
            if horizontal_window[0] in ('X', 'S'):
                if ''.join(horizontal_window) in ("XMAS", "SAMX"):
                    total += 1
    return total

def find_xmas_diagonal(input_map):
    total = 0
    for row in input_map:
        print()


if __name__ == "__main__":
    main()