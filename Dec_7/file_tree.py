""" 
--- Day 7: No Space Left On Device ---
Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

"""
from typing import Dict, List, Tuple

# #initilize our cache and dir trackers
# filesystem_dict: Dict[str, int] ={}
# curr_dir: str = ''

# # use stack to track history
# history=[]

# # use dict to track recurring ls calls in the same directory (avoid doublecounts)
# ls_called: Dict[str, int] = {}

# def parse_files_to_dict (terminal_output: str):
#     global curr_dir, history, ls_called

#     # if moving up through file system
#     if terminal_output[0:6] == '$ cd .' and len(history) > 1:
#         print("terminal_output[0:6]: ", terminal_output[0:6], "history before pop: ", history)

#         # reassign curr dir from history
#         history.pop()
#         curr_dir_info = history.pop()
#         curr_dir = curr_dir_info[0]
#         print("curr_dir_info after cd .. (pop): ", curr_dir_info, "curr_dir_info[0]: ", curr_dir_info[0],  "curr_dir_info[1]: ", curr_dir_info[1], )
        
#         # add the previous dir's size to the parent's size
#         print("filesystem BEFORE previous dir's filesizes added: ", filesystem_dict[curr_dir])
#         filesystem_dict[curr_dir] += curr_dir_info[1]
#         print("filesystem AFTER previous dir's filesizes added: ", filesystem_dict[curr_dir])
#         return "Done"

#     # if moving down through file system
#     if terminal_output[0:3] == '$ c' and terminal_output[6] != '.':
#         print("terminal_output[0:3]: ", terminal_output[0:3])

#         # reassign curent directory using slice on input
#         curr_dir = terminal_output[5:].strip()
#         history.append([curr_dir, 0])
#         ls_called[curr_dir] = ls_called.get(curr_dir, 0)
#         filesystem_dict[curr_dir] = filesystem_dict.get(curr_dir, 0)
#         print("curr_dir from string slice", curr_dir, "dir_history with curr adeded: ", history)

#     # if list command is called
#     if terminal_output[0:3] == '$ l':
#         ls_called[curr_dir] += 1
#         print("ls_called: ", ls_called)

#     # # confirm that the list command hasn't yet been called in this directory (avoid doublecounts)
#     if ls_called[curr_dir] <= 1 and len(history) > 1:
#         print("ls_called <= 1: ", "yes")

#         #now add the file sizes
#         if terminal_output[0].isnumeric():
#             # pull digits from string and convert them into integer
#             size_array_of_digits = [i for i in terminal_output.split() if i.isdigit()]
#             size_str = ''.join(map(str, size_array_of_digits))
#             size_int = int(size_str)

#             # add the filesize to the histroy and dict under the current directory
#             history[-1][1] += size_int
#             filesystem_dict[curr_dir] = filesystem_dict.get(curr_dir, 0) + size_int
#             print("file size added to filesystem dic under current directory: ", history)

# print(filesystem_dict)

# def sum_deletion_cadidate_sizes (filesystem: Dict[str, int], target_size: int ) -> int:
#     # extract filesizes from dict
#     directory_sizes = filesystem.values()
#     print("directory_sizes: ", directory_sizes)

#     # make list of file sizes that match target
#     deletion_candidates = list(filter(lambda v: v <= target_size, directory_sizes))
#     print("deletion candidates: ", deletion_candidates)

#     # reduce array to sum of values and return total
#     total = sum(deletion_candidates)
#     return total

# # read datafile line by line
# with open("/Users/fleigh/Projects/AdventofCode/Dec_7/Data.txt") as f:
#     for line in f:
#         print(line)
#         parse_files_to_dict(line)

#     # after parsing entire file, find the sum of the rightly sized directories
#     max_size = 100000
#     memory_to_clean = sum_deletion_cadidate_sizes(filesystem_dict, max_size)
#     print(memory_to_clean) # too low: 1149206/ 1283925

# --------------------------------------------------------------------------------------------

# # initialize our cache and dir trackers
# filesystem_dict: Dict[str, int] ={}
# curr_dir: str = ''
# previous_command: str = ''
# curr_dir_sum: int = 0

# # use stack to track history
# sum_history: List[int] = [] # consider replacing with history: List[Tuple[str, int]]=[]
# dir_history: List[str] = []

# # use dict to track recurring ls calls in the same directory (avoid doublecounts)
# ls_called: Dict[str, int] = {}

# def parse_files_to_dict (terminal_output: str):
#     global curr_dir, curr_dir_sum, sum_history, dir_history, ls_called, previous_command

#     # if moving up through file system
#     if terminal_output[0:6] == '$ cd .' and len(dir_history) > 1:
#         print("terminal_output[0:6]: ", terminal_output[0:6], "dir_histroy: ", dir_history)

#         # reset the sum counter for a new dir
#         sum_history.append(curr_dir_sum)
#         curr_dir_sum = 0
#         print("sum_history: ", sum_history, "curr_dir_sum back to zero: ", curr_dir_sum)

#         # reassign curr dir from history
#         dir_history.pop()
#         curr_dir = dir_history.pop()
#         print("curr_dir from history pop: ", curr_dir, "dir_histroy with curr removed: ", dir_history)
        
#         # add the previous dir's size to the parent's size
#         print("filesystem before previous dir's filesizes added (a): ", filesystem_dict)
#         filesystem_dict[curr_dir] += sum_history.pop()
#         print("filesystem with previous dir's filesizes added: ", filesystem_dict[curr_dir])
#         return "Done"

#     # if moving down through file system
#     if terminal_output[0:3] == '$ c' and terminal_output[6] != '.':
#         print("terminal_output[0:3]: ", terminal_output[0:3])

#         # reset the sum counter for a new dir
#         sum_history.append(curr_dir_sum)
#         curr_dir_sum = 0
#         print("sum_history", sum_history, "curr_dir_sum back to zero: ", curr_dir_sum)

#         # reassign curent directory using slice on input
#         curr_dir = terminal_output[5:].strip()
#         dir_history.append(curr_dir)
#         ls_called[curr_dir] = ls_called.get(curr_dir, 0)
#         filesystem_dict[curr_dir] = filesystem_dict.get(curr_dir, 0)
#         print("curr_dir from string slice", curr_dir, "dir_history with curr adeded: ", dir_history)

#     # if list command is called
#     if terminal_output[0:3] == '$ l':
#         ls_called[curr_dir] += 1
#         print("ls_called: ", ls_called)

#     # # confirm that the list command hasn't yet been called in this directory (avoid doublecounts)
#     if ls_called[curr_dir] <= 1:
#         print("ls_called <= 1: ", "yes")

#         #now add the file sizes
#         if terminal_output[0].isnumeric():
#             # pull digits from string and convert them into integer
#             size_array_of_digits = [i for i in terminal_output.split() if i.isdigit()]
#             size_str = ''.join(map(str, size_array_of_digits))
#             size_int = int(size_str)
#             curr_dir_sum += size_int #to be added to histroy stack elsewhere
#             print("file size added to current dir sum: ", curr_dir_sum)

#             # add the filesize to the dict under the current directory
#             filesystem_dict[curr_dir] = filesystem_dict.get(curr_dir, 0) + size_int
#             print("file size added to filesystem dic under current directory: ", curr_dir_sum)

# print(filesystem_dict)

# def sum_deletion_cadidate_sizes (filesystem: Dict[str, int], target_size: int ) -> int:
#     # extract filesizes from dict
#     directory_sizes = filesystem.values()
#     print("directory_sizes: ", directory_sizes)

#     # make list of file sizes that match target
#     deletion_candidates = list(filter(lambda v: v <= target_size, directory_sizes))
#     print("deletion candidates: ", deletion_candidates)

#     # reduce array to sum of values and return total
#     total = sum(deletion_candidates)
#     return total

# # read datafile line by line
# with open("/Users/fleigh/Projects/AdventofCode/Dec_7/Data.txt") as f:
#     for line in f:
#         print(line)
#         parse_files_to_dict(line)

#     # after parsing entire file, find the sum of the rightly sized directories
#     max_size = 100000
#     memory_to_clean = sum_deletion_cadidate_sizes(filesystem_dict, max_size)
#     print(memory_to_clean)
