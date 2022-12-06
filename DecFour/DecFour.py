"""
    --- Day 4: Camp Cleanup ---
Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.
However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).
For example, consider the following list of section assignment pairs:
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
For the first few pairs, this list means:
Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
The Elves in the second pair were each assigned two sections.
The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.
This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8
Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?

"""

def find_full_overlap(range_pair: str):
    """this function identifies the pairs of ranges that fully overlap (one range fully contains the other)
    Args:
        range_pair (str): a pair of ranges with the format: "x1-x2,y1-y2"
    Returns: 
        count_overlap (int): the sum of pairs that have fully overlapping ranges
    """

    # initilize the range overlap
    full_overlap = False

    # grab the front and end alues for each elf in par by deliminating by comma and dash
    # need to use strip to remove trailing spaces
    pair = line.strip().replace("-", ",").split(",")
    elf1_start = int(pair[0])
    elf1_end = int(pair[1])
    elf2_start = int(pair[2])
    elf2_end = int(pair[3])
    # determine if full overlap occurs
    full_overlap_of_elf1 = elf1_end <= elf2_end and elf1_start >= elf2_start
    full_overlap_of_elf2 = elf2_end <= elf1_end and elf2_start >= elf1_start
    
    #if there was full overlap, increase the count
    if full_overlap_of_elf1 or full_overlap_of_elf2:
        full_overlap = True

    return full_overlap

sum_full_overlap = 0
# read datafile line by line
with open("/Users/fleigh/Projects/AdventofCode/DecFour/DecFour.txt") as f:
    for line in f:
        if find_full_overlap(line):
            sum_full_overlap += 1

print(sum_full_overlap)

"""
--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?

"""

def find_partial_overlap(range_pair: str):
    """this function identifies the pairs of ranges that have any overlap (partial or full)
    Args:
        range_pair (str): a pair of ranges with the format: "x1-x2,y1-y2"
    Returns: 
        count_overlap (int): the sum of pairs that have overlapping ranges
    """

    # initilize the overlap setting to false
    partial_overlap = False

    # grab the front and end alues for each elf in par by deliminating by comma and dash
    # need to use strip to remove trailing spaces
    # structure of result is [x1, x2, y1, y2]
    pair = line.strip().replace("-", ",").split(",")
    elf1_start = int(pair[0])
    elf1_end = int(pair[1])
    elf2_start = int(pair[2])
    elf2_end = int(pair[3])
    # calcualte amount of overlap
    overlap = min(elf1_end, elf2_end) - max(elf1_start, elf2_start)
    
    # if the amount of overlap is greater than or equal to zero, increment the count
    # an overlap of 0 indicates an overlap unit of 1
    if overlap >= 0:
        partial_overlap = True

    return partial_overlap

sum_partial_overlap = 0
# read datafile line by line
with open("/Users/fleigh/Projects/AdventofCode/DecFour/DecFour.txt") as f:
    for line in f:
        sum_partial_overlap += find_partial_overlap(line)

print(sum_partial_overlap)