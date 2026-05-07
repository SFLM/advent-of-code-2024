def main():
    with open("input.txt") as f:
        raw = f.read().split("\n\n")
    
    page_ordering_rules, updates = raw

    solution1(page_ordering_rules.split(), updates.split())
    solution2(page_ordering_rules.split(), updates.split())

def solution1(page_ordering_rules, updates):
    rules_dict = create_rules_dict(page_ordering_rules)
    correct_updates = [update.split(',') for update in updates if not first_incorrect_position(rules_dict, update.split(','))]
    total = sum(int(correct_update[len(correct_update)//2]) for correct_update in correct_updates)
    print(total)

def solution2(page_ordering_rules, updates):
    rules_dict = create_rules_dict(page_ordering_rules)
    incorrect_updates = []
    incorrect_positions = []
    correct_updates = []
    
    for update in updates:
        if incorrect_position := first_incorrect_position(rules_dict, update.split(',')):
            incorrect_updates.append(update)
            incorrect_positions.append(incorrect_position)
    
    for id, incorrect_update in enumerate(incorrect_updates):
        correct_updates.append(recursive_fix_update(rules_dict, incorrect_update.split(','), incorrect_positions[id]))
    
    total = sum(int(correct_update[len(correct_update)//2]) for correct_update in correct_updates)

    print(total)

def create_rules_dict(input_rules):
    result = dict()
    for rule in input_rules:
        rule_left, rule_right = rule.split('|')
        result.setdefault(rule_left, []).append(rule_right)
    return result

def first_incorrect_position(rules_dict, update_input):
    for position, page in enumerate(update_input):
        if page in rules_dict.keys():
            if set(update_input[:position]) & set(rules_dict[page]): # Cool intersection
                return position
    return False

def recursive_fix_update(rules_dict, update, wrong_position):
    if not wrong_position:
        return update
    pivot = update[wrong_position]
    update.remove(pivot)
    for insert_position, page in enumerate(update[:wrong_position]):
        if page in rules_dict[pivot]:
            new_update = update[:insert_position]+[pivot]+update[insert_position:]
            return recursive_fix_update(rules_dict, new_update, first_incorrect_position(rules_dict, new_update))
    

if __name__ == "__main__":
    main()