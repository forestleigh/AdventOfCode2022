""" 
--- Day 6: Tuning Trouble ---
How many characters need to be processed before the first start-of-packet marker is detected?

"""

def nonrepeating_substring(datastream: str, mode: int):
    """ This function identifies the first nonrepeating substring of length 4 in the input string
    Args:
        datastream (str): this is a string of seemingly random chars from the elves
        mode (int): length of nonrepeating substring desired 
    Returns: 
        marker_index (int): this is the index of datastream at the end of the first nonrepeating substring
    """

    # initilize window and marker index
    window_left = 0
    window_right = 0
    substring_set = set()

    while window_right < len(datastream):
        # if the newsest char is already in the set
        if datastream[window_right] in substring_set:
            # remove the value for window_left from the set
            substring_set.remove(datastream[window_left])
            # shift the left window forward
            window_left += 1
        # if the newset char is not already in the set
        else:
            # add it to the set
            substring_set.add(datastream[window_right])
            # once the set has 4 chars
            if len(substring_set) == mode:
                # return the marker index (outer window plus 1 for zeroth index)
                return window_right + 1
            # shift the right window forward
            window_right += 1

with open("/Users/fleigh/Projects/AdventofCode/Dec_6/Data.txt") as f:
    data = f.read()
print(nonrepeating_substring(data, 4))

""" 
--- Part Two ---
How many characters need to be processed before the first start-of-message marker is detected?

"""
print(nonrepeating_substring(data, 14))