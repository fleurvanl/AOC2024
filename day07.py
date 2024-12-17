from itertools import product

from utils.file_handling import FileHandling


def calculate(components, combination):
    result = int(components[0])
    for i, operator in enumerate(combination):
        if operator == '*':
            result *= int(components[i + 1])
        elif operator == '+':
            result += int(components[i + 1])
        elif operator == '|':
            result = int(str(result) + components[i + 1])
    return result


def main():
    file = FileHandling.read_file('input/day07.txt')
    lines = file.split('\n')

    operations = ['*', '+']

    first_star = 0

    for line in lines:
        if line != '':
            solution, numbers = line.split(': ')
            numbers = tuple(numbers.split(' '))
            # Generate all possible combinations of operators
            operator_combinations = list(product(operations, repeat=len(numbers) - 1))
            for combination in operator_combinations:
                calculation = calculate(numbers, combination)
                if int(solution) == calculation:
                    first_star += calculation
                    break

    print(f'first star: {first_star}')

    operations = ['*', '+', '|']

    second_star = 0

    for line in lines:
        if line != '':
            solution, numbers = line.split(': ')
            numbers = numbers.split(' ')
            # Generate all possible combinations of operators
            operator_combinations = list(product(operations, repeat=len(numbers) - 1))
            for combination in operator_combinations:
                calculation = calculate(numbers, combination)
                if int(solution) == calculation:
                    second_star += calculation
                    break
    if second_star <= 10236216964378:
        print('answer too low')
    print(f'second star: {second_star}')


if __name__ == '__main__':
    main()
