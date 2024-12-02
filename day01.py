from utils.file_handling import FileHandling


def calculate_total_distance(left, right):
    # find minimum values, compare difference and add to total distance
    total_distance = 0
    while left:
        min_left = min(left)
        min_right = min(right)
        total_distance += abs(min_left - min_right)
        left.remove(min_left)
        right.remove(min_right)
    return total_distance


def calculate_similarity_score(left, right):
    similarity_score = 0
    for number in left:
        amount = right.count(number)
        similarity_score += (amount * number)
    return similarity_score


def main():
    file = FileHandling.read_file('input/day01.txt')
    lines = file.split('\n')
    # make 2 dicts (left and right) in shape {index: item}
    left = []
    right = []
    for i, line in enumerate(lines):
        if line:
            numbers = line.split('   ')
            left.append(int(numbers[0]))
            right.append(int(numbers[1]))
    # STAR 1!
    total_distance = calculate_total_distance(left.copy(), right.copy())
    print(f'first star: {total_distance}')
    # STAR 2!
    similarity_score = calculate_similarity_score(left, right)
    print(f'second star: {similarity_score}')


if __name__ == "__main__":
    main()
