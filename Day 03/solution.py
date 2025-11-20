import re

def main():
    with open("input.txt") as f:
        raw = f.read()
    
    solution1(raw)
    solution2(raw)

def solution1(input):
    total = 0
    mul_instructions = re.findall(r"(?<=mul\()(\d{1,3}),(\d{1,3})(?=\))", input)
    for mul_instruction in mul_instructions:
        total += int(mul_instruction[0]) * int (mul_instruction[1])
    
    print(f"Solution 1: {total}")

def solution2(input):
    total = 0
    instructions = re.findall(r"(?<=mul\()\d{1,3},\d{1,3}(?=\))|do\(\)|don't\(\)", input)
    enabled = True
    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif enabled:
            leftNumber, rightNumber = instruction.split(',')
            total += int(leftNumber)*int(rightNumber)
    print(f"Solution 2: {total}")

if __name__ == "__main__":
    main()