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


def organise_per_file(empty_space_disk_map):
    per_file_disk_map = []
    file = []
    for i in range(len(empty_space_disk_map) - 1):
        file.append(empty_space_disk_map[i])
        # check if the occupied file is the same as the next, if not, it's a new file/empty space, so we append this
        # file to the disk map and start a new file
        if empty_space_disk_map[i] != empty_space_disk_map[i + 1]:
            per_file_disk_map.append(file)
            file = []
        else:
            continue
    file.append(empty_space_disk_map[-1])
    per_file_disk_map.append(file)
    return per_file_disk_map


def find_file(per_file_disk_map, size, current_index):
    # iterating backwards
    for i in range(len(per_file_disk_map) - 1, -1, -1):
        # if we find a file that fits
        if per_file_disk_map[i][-1] != None:
            if len(per_file_disk_map[i]) <= size:
                # make sure we don't return files that have already been moved forward
                if i > current_index:
                    return per_file_disk_map[i], i
                else:
                    return None, None
    # if we find nothing
    return None, None


# def merge_empty_files(per_file_disk_map):
#     clean_file = []
#     for i, file in enumerate(per_file_disk_map):
#         if file[-1] == None:
#             none_file = file
#             while per_file_disk_map[i + 1][-1] == None:
#                 none_file.extend(per_file_disk_map[i + 1])
#                 per_file_disk_map.pop(i + 1)
#             clean_file.append(none_file)
#         else:
#             clean_file.append(file)
#     return clean_file


def insert_nones(per_file_disk_map, size, index):
    # check if the files before or after are also empty, if so, we extend them so we avoid having multiple empty files
    if index > 0:
        if per_file_disk_map[index - 1][0] == None:
            per_file_disk_map[index - 1].extend([None for _ in range(size)])
    if index + 1 < len(per_file_disk_map):
        if per_file_disk_map[index + 1][0] == None:
            per_file_disk_map[index + 1].extend([None for _ in range(size)])
    # if there are no other empty files, we just replace the old file
    else:
        per_file_disk_map[index] = [None for _ in range(size)]
    return per_file_disk_map


def move_data_per_file(per_file_disk_map):
    for i, file in enumerate(per_file_disk_map):
        # check if there's a file or empty space
        if file[-1] == None:
            # if it's empty, start looking for a file that fits here
            size = len(file)
            replacement, index = find_file(per_file_disk_map, size, i)
            # replace file,
            if replacement != None and index != None:
                per_file_disk_map[i] = replacement
                # the space that is left behind gets filled with Nones
                per_file_disk_map = insert_nones(per_file_disk_map, len(replacement), index)
                # per_file_disk_map[index + 1] = [None for _ in range(len(replacement))]
                # if the file was smaller than the empty space, we need to insert more Nones
                if size > len(replacement):
                    per_file_disk_map = insert_nones(per_file_disk_map, size - len(replacement), i + 1)
                    # per_file_disk_map.insert(i + 1, [None for _ in range(size - len(replacement))])
            else:
                continue
        else:
            continue
    return per_file_disk_map




def main():
    disk_map = FileHandling.read_file('input/day09.txt')
    empty_space_disk_map = visualise_space(disk_map)
    reorganised_disk_map = move_data(empty_space_disk_map)
    check_sum = calculate_checksum(reorganised_disk_map)
    print(f'first star: {check_sum}')

    per_file_disk_map = organise_per_file(empty_space_disk_map)
    reorganised_per_file_disk_map = move_data_per_file(per_file_disk_map)

if __name__ == '__main__':
    main()
