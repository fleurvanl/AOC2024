from utils.file_handling import FileHandling


def visualise_space(disk_map):
    empty_space_disk_map = []
    block_number = 0
    for index in range(len(disk_map)):
        # the even index numbers show there's a block file
        if index % 2 == 0:
            for i in range(int(disk_map[index])):
                empty_space_disk_map.append(block_number)
            block_number += 1
        else:
            # the odd index numbers show empty space
            if index % 2 == 1:
                for i in range(int(disk_map[index])):
                    empty_space_disk_map.append(None)

    return empty_space_disk_map


def main():
    disk_map = FileHandling.read_file('input/day09.txt')
    empty_space_disk_map = visualise_space(disk_map)


if __name__ == '__main__':
    main()
