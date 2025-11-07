def main():
    with open("input.txt") as f:
        pairs = [[int(char) for char in line.split()] for line in f.read().splitlines()]
    
    solution_1(pairs)

def solution_1(pairs_par):
    left_list = []
    right_list = []
    
    for pair in pairs_par:
        left_list.append(pair[0])
        right_list.append((pair[1]))

    left_list.sort()
    right_list.sort()

    difference = 0
    for i in range(len(left_list)):
        difference += abs(left_list[i]-right_list[i])

    print(f"Solution 1: {difference}")


if __name__ == "__main__":
    main()