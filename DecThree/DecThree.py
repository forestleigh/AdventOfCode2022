"""
    --- Day 3: Rucksack Reorganization ---
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.
Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.
The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).
The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
The fourth rucksack's compartments only share item type v.
The fifth rucksack's compartments only share item type t.
The sixth rucksack's compartments only share item type s.
To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

"""

# make a dict of priorities for lower case items (a-z -> 1-26)
from string import ascii_letters
priorities_map = {v: k for k, v in enumerate(ascii_letters, 1)}
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6...

def rucksack_reorg(path_to_data):
    """this function identifies the items that are in both compartments of a rucksack and adds their respective priorties
    Args:
        path_to_data (str): describes path to text file with data
    Returns: 
        sum_of_priorities (int): the sum of priorties for each item type that appears in both compartments of each rucksack
    """

    # initiate the cumulative list of shared items and priorities total
    shared_items = []
    priorities_of_shared_total = 0

    # read datafile line by line
    with open(path_to_data, "r") as f:
        for line in f:
            # initilize current shared items
            current_shared_items = {}

            # the length of string is always even so can split with simple indexing
            first_half = line[0: len(line)//2]
            second_half = line[len(line)//2: len(line)]

            # create hash map for first_half
            first_half_map = {}
            for char in first_half:
                first_half_map[char] = char

            # itterate through second half and look for values in the map
            for char in second_half:
                # if the item is in the first list
                if first_half_map.get(char, False):
                    # add to current shared items for this rucksack
                    current_shared_items[char] = char

            # add the item to our shared items list
            shared_items += current_shared_items

        # finnaly, calcualte the priorities
        for item in shared_items:
                # add priotrity to the accumulaating total
                priorities_of_shared_total += priorities_map[item]

    # return the sum of all priotiries of the items shared by compartments in single ruckshacks
    return priorities_of_shared_total


print(rucksack_reorg("/Users/fleigh/Projects/AdventofCode/DecThree/DecThree.txt"))

"""
    --- Part Two ---
As you finish identifying the misplaced items, the Elves come to you with another issue.
For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves. That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.
The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.
Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the above example, the first group's rucksacks are the first three lines:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
And the second group's rucksacks are the next three lines:

wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges. In the second group, their badge item type must be Z.

Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

"""


def rucksack_reorg_by_three(path_to_data):
    """this function identifies the items that are in both compartments of a rucksack and adds their respective priorties
    Args:
        path_to_data (str): describes path to text file with data
    Returns: 
        sum_of_priorities (int): the sum of priorties for each item type that appears in both compartments of each rucksack
    """

    # initilize the accumulator
    priorities_total = 0

    # read datafile line by line
    with open(path_to_data, "r") as f:
        lines = f.read().splitlines()

        #iterate over groups of 3 lines
        for i in range(0, len(lines), 3):
            # make each sack into a set to remove duplicates
            elf1 = set(lines[i + 0])
            elf2 = set(lines[i + 1])
            elf3 = set(lines[i + 2])

            # find the intersection of the 3 elf's sacks
            common_el = elf1.intersection(elf2).intersection(elf3)
            badge_id = list(common_el)[0]

            # add the priortiy score to total
            priorities_total += priorities_map[badge_id]

        return priorities_total


print(rucksack_reorg_by_three("/Users/fleigh/Projects/AdventofCode/DecThree/DecThree.txt"))