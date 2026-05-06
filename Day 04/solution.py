from collections import deque

def main():
    with open("input.txt") as f:
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
    total += find_xmas_diagonal(input_map) # Main diagonal
    total += find_xmas_diagonal(list(zip(*input_map[::-1]))) # Antidiagonal

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
    for row_number in range(len(input_map)-3):
        for letter_number in range(len(input_map[0])-3):
            if (first_letter := input_map[row_number][letter_number]) in ('X', 'S'):
                last_three_letters = input_map[row_number+1][letter_number+1] + input_map[row_number+2][letter_number+2] + input_map[row_number+3][letter_number+3]
                if first_letter + last_three_letters in ("XMAS", "SAMX"):
                    total += 1
    return total


if __name__ == "__main__":
    main()