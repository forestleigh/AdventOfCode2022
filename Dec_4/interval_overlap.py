"""
--- Day 4: Camp Cleanup ---
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
    pair = range_pair.strip().replace("-", ",").split(",")
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
with open("/Users/fleigh/Projects/AdventofCode/Dec_4/Data.txt") as f:
    for line in f:
        if find_full_overlap(line):
            sum_full_overlap += 1

print(sum_full_overlap)

"""
--- Part Two ---
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
    pair = range_pair.strip().replace("-", ",").split(",")
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
with open("/Users/fleigh/Projects/AdventofCode/Dec_4/Data.txt") as f:
    for line in f:
        sum_partial_overlap += find_partial_overlap(line)

print(sum_partial_overlap)