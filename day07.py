from itertools import product

from utils.file_handling import FileHandling


def calculate(components, combination):
    result = int(components[0])
    for i, operator in enumerate(combination):
        if operator == '*':
            result *= int(components[i + 1])
        elif operator == '+':
            result += int(components[i + 1])
    return result


def main():
    file = FileHandling.read_file('input/day07.txt')
    lines = file.split('\n')

    operations = ['*', '+']

    first_star = 0

    for line in lines:
        if line != '':
            solution, components = line.split(': ')
            components = tuple(components.split(' '))
            # Generate all possible combinations of operators
            operator_combinations = list(product(operations, repeat=len(components) - 1))
            for combination in operator_combinations:
                calculation = calculate(components, combination)
                if int(solution) == calculation:
                    first_star += calculation
                    break

    print(f'first star: {first_star}')

    operations = ['*', '+', '|']

    second_star = 0

    for line in lines:
        if line != '':
            solution, components = line.split(': ')
            components = components.split(' ')
            # Generate all possible combinations of operators
            operator_combinations = list(product(operations, repeat=len(components) - 1))
            for combination in operator_combinations:
                while '|' in combination:
                    # find indexes of |
                    # this is gonna mess up the indices if we remove |
                    index = combination.index('|')
                    # join number at that index and the next
                    # remove | from combination
                calculation = calculate(components, combination)
                if int(solution) == calculation:
                    second_star += calculation
                    break



if __name__ == '__main__':
    main()
