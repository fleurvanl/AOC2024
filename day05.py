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


def check_order(update, ordering_rules):
    # find relevant rules per update
    relevant_rules = defaultdict(list)
    for i, page_number in enumerate(update):
        for rule in ordering_rules:
            if page_number in rule:
                relevant_rules[page_number].append(rule)
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


def main():
    file = FileHandling.read_file('input/day05.txt')
    lines = file.split('\n')
    ordering_rules, updates = organise_data(lines)
    correct_updates = []
    # loop over updates
    for update in updates:
        update = update.split(',')
        if check_order(update, ordering_rules):
            correct_updates.append(int(update[(len(update)//2)]))
    print(f'first star: {sum(correct_updates)}')





if __name__ == '__main__':
    main()
