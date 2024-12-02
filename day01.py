from utils.file_handling import FileHandling


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
    # find minimum value
    total_distance = 0
    while left:
        min_left = min(left)
        min_right = min(right)
        total_distance += abs(min_left - min_right)
        left.remove(min_left)
        right.remove(min_right)
    print(f'first star: {total_distance}')



if __name__ == "__main__":
    main()
