def main():
    with open("input.txt") as f:
        raw_reports = f.read().splitlines()

    solution_1(raw_reports)
    solution_2(raw_reports)

def is_safe(report_levels):
    delta = None
    last_level = None
    for current_level in report_levels:
        if not last_level:
            last_level = current_level
            continue
        difference = last_level - current_level
        if not (0 < abs(difference) <= 3):
            return False
        last_level = current_level
        if not delta:
            delta = difference
            continue
        if (delta < 0) != (difference < 0):
            return False
    return True

def solution_1(reports_input):
    safe_reports = 0
    for report in reports_input:
        levels = [int(raw_level) for raw_level in report.split()]
        if is_safe(levels):
            safe_reports += 1
    
    print(f"Solution 1: {safe_reports}")

def solution_2(reports_input):
    safe_reports = 0
    for report in reports_input:
        levels = [int(raw_level) for raw_level in report.split()]
        if is_safe(levels):
            safe_reports += 1
        else:
            for i in range(len(levels)):
                dampened_levels = levels[:i] + levels[i+1:]
                if is_safe(dampened_levels):
                    safe_reports += 1
                    break
      
    print(f"Solution 2: {safe_reports}")

if __name__ == "__main__":
    main()