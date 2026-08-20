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
    total_calibration_result = 0
    
    for line in input:
        test_value_raw, equation_numbers_raw = line.split(": ")
        test_value = int(test_value_raw)
        equation_numbers = [int(number) for number in equation_numbers_raw.split()]
        if can_solve(test_value, equation_numbers, 1, equation_numbers[0], True):
            total_calibration_result += test_value

    print(f"Solution 2: {total_calibration_result}")


def can_solve(test_value, equation_numbers, index, total, concatenate=False):
    if (index == len(equation_numbers)):
        if (total == test_value):
            return True
        return False

    if can_solve(test_value, equation_numbers, index+1, total+equation_numbers[index], concatenate):
        return True
    else:
        if can_solve(test_value, equation_numbers, index+1, total*equation_numbers[index], concatenate):
            return True
        if concatenate:
            concatenated = str(total) + str(equation_numbers[index])
            return can_solve(test_value, equation_numbers, index+1, int(concatenated), concatenate)
    


if __name__ == "__main__":
    main()