""" 
--- Day 7: No Space Left On Device ---
Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

"""
from typing import Dict, Union, Optional
import attr
import os

# initilize class defintiion for tree 
@attr.s(auto_attribs=True)
class dir:
    parent: Optional[dir]
    children: Dict[str, Union[dir, int]]
    name: str

# interpret commands of filesystem and call build tree function when relevant 
def parse_filesystem (array_of_files, root):
    line_count: int = 0
    current_dir: dir = root

    while line_count < len(array_of_files):
        # print('line count: ', line_count)

        # jumpt to root of tree
        if array_of_files[line_count] == '$ cd /':
            current_dir = root
            line_count += 1

        # jump to parent directory in tree
        elif array_of_files[line_count] == '$ cd ..':
            current_dir = current_dir.parent
            line_count += 1

        # jump to child directory in tree
        elif array_of_files[line_count].startswith('$ cd'):
            split_line: list = array_of_files[line_count].split()
            assert len(split_line) == 3
            current_dir_name: str = split_line[2]
            current_dir = current_dir.children[current_dir_name]
            line_count += 1

        # expand the tree with new children
        elif array_of_files[line_count] == '$ ls':
            line_count = parse_ls(array_of_files, line_count + 1, current_dir)

        else: 
            raise RuntimeError(f"invalid line | {array_of_files[line_count]}")

    return root

# function that builds tree (assumes ls is always caleld before a directory is visitied)
def parse_ls (array_of_files, line_count, current_dir):

    while line_count < len(array_of_files)  and not array_of_files[line_count].startswith('$'):
        split_line: list = array_of_files[line_count].split()
        assert len(split_line) == 2

        if array_of_files[line_count].startswith('dir'):
            new_dir_name: str = split_line[1]
            current_dir.children[new_dir_name] = dir(parent=current_dir, children={}, name = new_dir_name)
            line_count += 1

        if array_of_files[line_count][0].isnumeric():
            split_line: list = array_of_files[line_count].split()
            assert len(split_line) == 2
            new_file_size: int = split_line[0]
            new_file_name: str = split_line[1]
            current_dir.children[new_file_name] = int(new_file_size)
            line_count += 1

    # returns line count of next '$'
    return line_count

# function that confirms tree was properly built
prints = []
def print_tree(curr, base_path):
    for name, child in curr.children.items():
        full_path = os.path.join(base_path, name)
        if isinstance(child, int):
            new_str = f"path: {full_path}, size: {child}"
            prints.append(new_str)
        else:
            print_tree(child, base_path = full_path)

# combine directory sizes that are below size limit
total_under_limit: int = 0
size_limit: int = 100000
def traverse_filesystem(current):
    global total_under_limit, size_limit
    curr_size: int = 0
    for _, item in current.children.items():
        if isinstance(item, int):
            curr_size += item
        else:
            curr_size += traverse_filesystem(item)
    if curr_size <= size_limit:
        total_under_limit += curr_size
    return curr_size


root: dir = dir(parent=None, children={}, name = '/')
with open("/Users/fleigh/Projects/AdventofCode/Dec_7/Data.txt") as f:
    puzzle = f.read().splitlines()

# call function to build tree
fs = parse_filesystem(puzzle, root)

# print tree to check
print_tree(root, "/")
for p in prints: print(p)

# call function to traverse tree and cacluate sizes
current_mem_used = traverse_filesystem(fs)
print('size of the root: ', current_mem_used)
print('sum of files under 100000 in size: ', total_under_limit)

"""

--- Part Two ---
Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?


"""
# find dir size to delete 
max_disk_space:int = 70000000
memory_needed:int = 30000000
max_current_mem_to_keep:int = max_disk_space - memory_needed
dir_size_to_delete:int = current_mem_used -max_current_mem_to_keep

# combine directory sizes that are above size limit
large_dirs: list = []
def size_dirs(current):
    global dir_size_to_delete
    curr_size: int = 0
    for _, item in current.children.items():
        if isinstance(item, int):
            curr_size += item
        else:
            curr_size += size_dirs(item)
    if curr_size >= dir_size_to_delete:
            large_dirs.append(curr_size)
        
    return curr_size

# call function to traverse tree and cacluate sizes
size_dirs(fs)
print('smallest file to delete: ', sorted(large_dirs)[0])
