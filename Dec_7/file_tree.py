""" 

--- Day 7: No Space Left On Device ---
You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?
The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device
Perhaps you can delete some files to make space for the update?

You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example: './DataEx.txt'

Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

"""

#initilize our cache and dir trackers
filesystem_dict ={}
curr_dir = ''
curr_dir_sum = 0
# use stack data structure to hold relevant histories
sum_history = []
dir_history = []

def parse_files_to_dict (terminal_output: str):
    # if moving up through file system
    if terminal_output[0:7] == '$ cd ..':
        # reset the sum counter for a new dir
        sum_history.append(curr_dir_sum)
        curr_dir_sum = 0
        # reassign curr dir from history
        curr_dir = dir_history.pop()
        # add the previous dir's size to the parent's size
        filesystem_dict[curr_dir] += sum_history.pop()

    # if moving down through file system
    if terminal_output[0:3] == '$ c':
        # reset the sum counter for a new dir
        sum_history.append(curr_dir_sum)
        curr_dir_sum = 0
        # use slice to get dirname
        curr_dir = terminal_output.slice(5)
        # add current dir to history 
        dir_history.append(curr_dir)

        print("curr_dir: ", curr_dir)
        print("dir_history: ", dir_history)

    # if the first index is numeric (i.e. a file with size is located)
    if terminal_output[0].isnumeric():
        # get the number from the string using List comprehension + isdigit() +split()
        size_array_of_digits = [i for i in terminal_output.split() if i.isdigit()]
        size_str = ''.join(map(str, size_array_of_digits))
        size_int = int(size_str)
        curr_dir_sum += size_int
        # add the value to curr_dict size in filesystem dict (add to dict if first instance)
        filesystem_dict[curr_dir] = filesystem_dict.get(curr_dir, 0) + size_int
    # implicit return (we ignore terminal outputs of dir or ls)

def sum_deletion_cadidate_sizes (filesystem, target_size):
    # extract filesizes from dict
    values_array = filesystem.values()
    # make list of file sizes that match target
    deletion_candidates = list(filter(lambda v: v <= target_size, values_array))
    # reduce array to sum of values and return total
    total = 0
    for size in deletion_candidates:
        total += size
    return total

# read datafile line by line
with open("/Users/fleigh/Projects/AdventofCode/Dec_7/DataEx.txt") as f:
    for line in f:
        print(line)
        print("[0:7]", [line[0:7]])
        parse_files_to_dict(line)

    # after parsing entire file, find the sum of the rightly sized directories
    max_size = 100,000
    memory_to_clean = sum_deletion_cadidate_sizes(filesystem_dict, max_size)

print(memory_to_clean)
