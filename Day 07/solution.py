def main():
    with open("input.txt") as f:
        raw = f.read().splitlines()
    
    solution1(raw)
    solution2(raw)


def solution1(input):
    total_calibration_result = 0

    for line in input:
        test_value_raw, equation_numbers_raw = line.split(": ")
        test_value = int(test_value_raw)
        equation_numbers = [int(number) for number in equation_numbers_raw.split()]
        if can_solve(test_value, equation_numbers, 1, equation_numbers[0]):
            total_calibration_result += test_value

    print(f"Solution 1: {total_calibration_result}")


def solution2(input):
    print()


def can_solve(test_value, equation_numbers, index, total):
    if (index == len(equation_numbers)):
        if (total == test_value):
            return True
        return False

    if can_solve(test_value, equation_numbers, index+1, total+equation_numbers[index]):
        return True
    else:
        return can_solve(test_value, equation_numbers, index+1, total*equation_numbers[index])
    


if __name__ == "__main__":
    main()