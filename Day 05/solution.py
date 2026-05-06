def main():
    with open("input.txt") as f:
        raw = f.read().split("\n\n")
    
    page_ordering_rules, updates = raw

    solution1(page_ordering_rules, updates)
    # solution2(raw)

def solution1(page_ordering_rules, updates):
    total = 0
    rules_dict = create_rules_dict(page_ordering_rules)

    for update_raw in updates.split():
        update = update_raw.split(',')
        error_found = False
        for position, page in enumerate(update):
            if page in rules_dict.keys():
                if set(update[:position]) & set(rules_dict[page]): # Cool intersection
                    error_found = True
                    break
        if not error_found:
            total += int(update[len(update)//2])
    
    print(total)

def solution2(input):
    print()

def create_rules_dict(input_rules):
    result = dict()
    for rule in input_rules.split():
        rule_left, rule_right = rule.split('|')
        result.setdefault(rule_left, []).append(rule_right)
    return result

if __name__ == "__main__":
    main()