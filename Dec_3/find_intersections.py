"""
--- Day 3: Rucksack Reorganization ---
Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

"""

# make a dict of priorities for lower case items (a-z -> 1-26)
from string import ascii_letters
priorities_map = {v: k for k, v in enumerate(ascii_letters, 1)}
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6...

def rucksack_reorg(sack: str):
    """this function identifies the common char to two halves of an input string
    Args:
        sack (str): a string of random letters where capitalization matters
    Returns: 
        sum_of_priorities (int): each common item has a prioritiy score associated with it, this is their sum
    """
    # initialize priority score
    priority = 0

    # split pack into two equal pockets
    pocket_size = int(len(sack) / 2)
    inventory_1 = set(sack[:pocket_size])
    inventroy_2 = set(sack[pocket_size:])

    # find the intersection of the two sack halves
    common_item = list(inventory_1.intersection(inventroy_2))[0]
    priority += priorities_map[common_item[0]]

    return priority

# read datafile line by line
with open("/Users/fleigh/Projects/AdventofCode/Dec_3/Data.txt") as f:
    priorities_total = 0
    for line in f:
        priorities_total += rucksack_reorg(line)
print(priorities_total)


"""
--- Part Two ---
Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

"""

def rucksack_reorg_by_three(list_of_items):
    """this function identifies the common item in each consecutive set of 3 strings
    Args:
        list_of_items (list): a list of strings where each consecultive set of 3 strings has once common char
    Returns: 
        sum_of_priorities (int): each common item has a priotriy value associated with it, this is the sum of all priority values 
    """

    # initialize priority score
    priorities_total = 0

    #iterate over groups of 3 lines
    for i in range(0, len(list_of_items), 3):
        # make each sack into a set to remove duplicates
        elf1 = set(list_of_items[i + 0])
        elf2 = set(list_of_items[i + 1])
        elf3 = set(list_of_items[i + 2])
        # find the intersection of the 3 elf's sacks
        common_el = elf1.intersection(elf2).intersection(elf3)
        badge_id = list(common_el)[0]
        # add the priortiy score to total
        priorities_total += priorities_map[badge_id]
    return priorities_total

# read datafile as a list
with open("/Users/fleigh/Projects/AdventofCode/Dec_3/Data.txt") as f:
    lines = f.read().splitlines()
    priorities_sum = rucksack_reorg_by_three(lines)

print(priorities_sum)