from utils.file_handling import FileHandling


def visualise_space(disk_map):
    empty_space_disk_map = []
    block_number = 0
    for index in range(len(disk_map)):
        if disk_map[index] != '\n':
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


def find_final_data(empty_space_disk_map, final_num_index):
    # loop over disk space backwards, starting from the known latest used space
    for item in range(final_num_index - 1, -1, -1):
        if empty_space_disk_map[item] is not None:
            # return the latest used space and its index
            return (empty_space_disk_map[item], item)



def move_data(empty_space_disk_map):
    # keep track of where we've looked at the end of the disk map so we don't have to keep iterating
    final_num_index = len(empty_space_disk_map)
    # loop over reorganised disk map
    for space_index in range(len(empty_space_disk_map)):
        # make sure the algorithm stops before it messes up the order again
        if space_index + 1 < final_num_index:
            # if there's an empty space, we find the last number in the disk map and move it here
            if empty_space_disk_map[space_index] is None:
                content, index = find_final_data(empty_space_disk_map, final_num_index)
                empty_space_disk_map[space_index] = content
                empty_space_disk_map[index] = None
                final_num_index = index
    return empty_space_disk_map


def calculate_checksum(reorganised_disk_map):
    multiplied_item_content = []
    for i in range(len(reorganised_disk_map)):
        content = reorganised_disk_map[i]
        if content is not None:
            multiplied_item_content.append(i * content)
    return sum(multiplied_item_content)


def main():
    disk_map = FileHandling.read_file('input/day09.txt')
    empty_space_disk_map = visualise_space(disk_map)
    reorganised_disk_map = move_data(empty_space_disk_map)
    check_sum = calculate_checksum(reorganised_disk_map)
    print(f'first star: {check_sum}')


if __name__ == '__main__':
    main()
