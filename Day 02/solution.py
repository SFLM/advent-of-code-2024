def main():
    with open("input.txt") as f:
        raw_reports = f.read().splitlines()

    solution_1(raw_reports)

def solution_1(reports_input):
    safe_reports = 0
    for report in reports_input:
        levels = [int(raw_level) for raw_level in report.split()]

        safe = True
        delta = None
        last_level = None
        for current_level in levels:
            if not last_level:
                last_level = current_level
                continue
            difference = last_level - current_level
            if not (0 < abs(difference) <= 3):
                safe = False
                break
            last_level = current_level
            if not delta:
                delta = difference
                continue
            if (delta < 0) != (difference < 0):
                safe = False
                break
        if safe:
            safe_reports += 1
    
    print(f"Solution 1: {safe_reports}")

if __name__ == "__main__":
    main()