import re

def main():
    with open("input.txt") as f:
        raw = f.read()
    
    solution_1(raw)

def solution_1(input):
    total = 0
    mul_instructions = re.findall("mul\((\d{1,3}),(\d{1,3})\)", input)
    for mul_instruction in mul_instructions:
        total += int(mul_instruction[0]) * int (mul_instruction[1])
    
    print(f"Solution 1: {total}")

def solution_2(input):
    print()

if __name__ == "__main__":
    main()