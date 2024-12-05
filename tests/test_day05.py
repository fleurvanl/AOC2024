from day05 import organise_data, check_order

import pytest


@pytest.fixture
def example():
    return '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75, 47, 61, 53, 29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''.split('\n')




def test_organise_data(example):
    ordering_rules, updates = organise_data(example)
    assert len(ordering_rules) == 21
    assert len(updates) == 6


def test_check_order(example):
    ordering_rules, updates = organise_data(example)
    correct_updates = []
    for update in updates:
        update = update.split(',')
        if check_order(update, ordering_rules):
            index = len(update) // 2
            correct_updates.append(int(update[index]))
    print(correct_updates)
    assert sum(correct_updates) == 143
