from collections import defaultdict

from utils.file_handling import FileHandling


def check_order(updates, ordering_rules):
    # loop over updates
    for update in updates:
        # find relevant rules per update
        relevant_rules = defaultdict(list)
        for i, number in enumerate(update):
            for rule in ordering_rules:
                if number in rule:
                    relevant_rules[number].append(rule)
            # check if they're located correctly
            # relevant_rules = {number:[[x, y], [x, y]]}
            for number_rule in relevant_rules[number]:
                # if the X = the number, check if the numbers earlier in the update correspond to Y, because then it
                # would be false
                if number_rule[0] == number:
                    if number_rule[1] in update[:i]:
                        return False
                # if Y is the number, check if the later numbers correspond to X because that would make it False
                if number[1] == number:
                    if number_rule[0] in update[i:]:
                        return False


def main():
    file = FileHandling.read_file('input/day04.txt')
    lines = file.split('\n')
    ordering_rules = []
    updates = []
    switch = False
    for line in lines:
        if line == '\n':
            switch = True
        if not switch:
            ordering_rules.append('|'.split(line))
        else:
            updates.append(line)
    check_order(updates, ordering_rules)



if __name__ == '__main__':
    main()
