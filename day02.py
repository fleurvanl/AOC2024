from utils.file_handling import FileHandling


def check_report(numbers):
    diffs = []
    for i, num in enumerate(numbers):
        if i is not len(numbers) - 1:
            diff_with_next = int(numbers[i]) - int(numbers[i + 1])
            diffs.append(diff_with_next)
            if diff_with_next > 3 or diff_with_next < -3:
                return False
    # if all positive: every step is a decrease
    if all(num > 0 for num in diffs):
        return True
    # if all negative: every step is an increase
    elif all(num < 0 for num in diffs):
        return True
    # if 0 in diffs, return False
    else:
        return False


def check_report_dampner(numbers, level):
    for i, num in enumerate(numbers):
        current_numbers = numbers.copy()
        current_numbers.pop(i)
        if check_report(current_numbers):
            return True
    return False


    # diffs = []
    # if level > 1:
    #     return False
    # for i, num in enumerate(numbers):
    #     if i is not len(numbers) - 1:
    #         diff_with_next = int(numbers[i]) - int(numbers[i + 1])
    #         diffs.append(diff_with_next)
    #         # check if this is right
    #         if diff_with_next == 0:
    #             level += 1
    #             numbers.pop(i + 1)
    #             if check_report_dampner(numbers, level):
    #                 return True
    #             else:
    #                 return False
    #         if diff_with_next > 3 or diff_with_next < -3:
    #             level += 1
    #             numbers.pop(i + 1)
    #             if check_report_dampner(numbers, level):
    #                 return True
    #             else:
    #                 return False
    #         if all(num > 0 for num in diffs) or all(num < 0 for num in diffs):
    #             continue
    #         else:
    #             level += 1
    #             numbers.pop(i + 1)
    #             if check_report_dampner(numbers, level):
    #                 return True
    #             else:
    #                 return False
    # # if all positive: every step is a decrease
    # if all(num > 0 for num in diffs):
    #     return True
    # # if all negative: every step is an increase
    # elif all(num < 0 for num in diffs):
    #     return True


def main():
    file = FileHandling.read_file('input/day02.txt')
    lines = file.split('\n')
    num_safe = 0
    for line in lines:
        if line:
            numbers = line.split(' ')
            safety = check_report(numbers)
            if safety:
                num_safe += 1
    print(f'first star: {num_safe}')
    num_safe_dampner = 0
    for line in lines:
        if line:
            numbers = line.split(' ')
            safety = check_report_dampner(numbers, level=0)
            if safety:
                num_safe_dampner += 1
    print(f'second star: {num_safe_dampner}')


if __name__ == "__main__":
    main()
