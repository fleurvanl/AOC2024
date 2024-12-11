from collections import defaultdict

from utils.file_handling import FileHandling


def organise_data(lines):
    ordering_rules = []
    updates = []
    switch = False
    for line in lines:
        if line != '':
            if not switch:
                ordering_rules.append(line.split('|'))
            else:
                updates.append(line)
        else:
            switch = True
    return ordering_rules, updates


def find_relevant_rules(update, ordering_rules):
    relevant_rules = defaultdict(list)
    for i, page_number in enumerate(update):
        for rule in ordering_rules:
            if page_number in rule:
                relevant_rules[page_number].append(rule)
    return relevant_rules


def check_order(update, ordering_rules):
    for i, page_number in enumerate(update):
        # find relevant rules per update
        relevant_rules = find_relevant_rules(update, ordering_rules)
        # check if they're located correctly
        # relevant_rules = {page_number:[[x, y], [x, y]]}
        for number_rule in relevant_rules[page_number]:
            # if the X = the page_number, check if the numbers earlier in the update correspond to Y, because then it
            # would be false
            if number_rule[0] == page_number:
                if number_rule[1] in update[:i]:
                    return False
            # if Y is the page_number, check if the later numbers correspond to X because that would make it False
            # if page_number[1] == page_number:
            else:
                if number_rule[0] in update[i:]:
                    return False
    return True


def check_rule(x, y, relevant_rules):
    for number_rule in relevant_rules[x]:
        if number_rule[1] == y:
            return True
        if number_rule[0] == y:
            return False
    for number_rule in relevant_rules[y]:
        if number_rule[0] == x:
            return True
        if number_rule[1] == x:
            return False
    # if there is no rule about these two numbers, the order is assumed to be fine
    return True


def sort_update(update, relevant_rules):
    # bubble-sort adjacent
    sorted = False
    while not sorted:
        sorted = True
        for i, page_number in enumerate(update):
            if page_number != update[-1]:
                if not check_rule(page_number, update[i + 1], relevant_rules):
                    update[i], update[i + 1] = update[i + 1], update[i]
                    sorted = False
    return update



def main():
    file = FileHandling.read_file('input/day05.txt')
    lines = file.split('\n')
    ordering_rules, updates = organise_data(lines)
    correct_updates = []
    incorrect_updates = []
    fixed_updates = []
    # find correct updates
    for update in updates:
        update = update.split(',')
        if check_order(update, ordering_rules):
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)
    # get the middle number for each correct update and add them up
    print(f'first star: {sum([int(update[len(update) // 2]) for update in correct_updates])}')
    # fix incorrect updates
    for update in incorrect_updates:
        relevant_rules = find_relevant_rules(update, ordering_rules)
        fixed_updates.append(sort_update(update, relevant_rules))
    print(f'first star: {sum([int(update[len(update) // 2]) for update in fixed_updates])}')


if __name__ == '__main__':
    main()
