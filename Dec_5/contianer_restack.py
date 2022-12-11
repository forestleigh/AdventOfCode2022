"""
--- Day 5: Supply Stacks ---
After the rearrangement procedure completes, what crate ends up on top of each stack?

"""
from collections import OrderedDict

def parse_stack_layer(container_layer: str, stacks: dict):
    """this function reads the map datafile to setup the initial state of the containers in the stacks
    Args:
        container_layer (str): a string that depicts a single layer of the containers 
        stacks (dict): this is the inital state stroage dictionary 
    Returns: 
        stacks_made (dict): return the most updated version of the inital state each round 
    """
    # first we parse the containers
    # initilize stack count
    stack_id = 1
    # lets add this into a dictionary with key's being stack number and values being a list with the container ids
    # looping to every 4th index to ignore unimportant empty strings
    for element in container_layer[1::4]:
        if element.isalpha():
            if stacks_made.get(stack_id, False):
                # if the stack id exists, append the element to the front of the list
                # need to use the insert method to add to the front of the list as we read down the file
                stacks_made[stack_id].insert(0, element)
            else:
                # add the stack id and pair it with a new list containting the element
                stacks_made[stack_id] = list(element)
        # increae stack id with each call
        stack_id += 1

    return stacks_made


def arrange_supply_stacks(instructions: str, stacks: dict, mode: str):
    """this function identifies which boxes will be at the top of each stack after a predefined rearrangement
    Args:
        line (str) : the instructions for how to rearange the containers in the stacks
        stack (dict) : the stacks and their containers for manupulation based on instructions
        mode (str) : the model of crane is either "9000" for picking up 1 box at a time and "9001" for pucking up many boxes at a time
    Returns: 
        top_boxes (str): a string with the simple letter names of each box on top of one of the stacks
    """
    # parse the str into a list delinitating on spaces
    # ex: ['move', '5', 'from', '3', 'to', '4']
    next_step = instructions.split()
    # get digits from the list
    # ex: [5, 3, 4]
    digit_list = [int(x) for x in next_step if x.isnumeric()]
    # destructure elements for legibity
    [count, src, dest] = digit_list

    if mode == "9000":
        # now to follow the instructions
        # repeat action for this many containers
        for i in range(count):
            # pop off container from list at digit_list[1]
            temp = stacks[src].pop()
            # push on container from list at digit_list[2]
            stacks[dest] += [temp]

    if mode == "9001":
        temp_list = []
        # repeat action for this many containers
        for i in range(count):
            # pop off container from list at digit_list[1]
            temp = stacks[src].pop()
            # push to temporary stack
            temp_list.insert(0, temp)
        # push on container from list at digit_list[2]
        stacks[dest] += temp_list


# initilize the stack dictionary
stacks_made = {}
# read datafile line by line
with open("/Users/fleigh/Projects/AdventofCode/Dec_5/Map.txt") as f:
    for line in f:
        stack_dict = parse_stack_layer(line, stacks_made)

# once inital state is parse the stack dict needs to be sorted
state_of_containers = OrderedDict(sorted(stack_dict.items()))

# read datafile line by line
with open("/Users/fleigh/Projects/AdventofCode/DecFifth/Instructions.txt") as f:
    for line in f:
        arrange_supply_stacks(line, state_of_containers, "9000")

# now identify the containers at the top of every stack
# initlizae the return stirng
top_boxes = ''
# itterate through the stacks collecting the top box of each
for k in state_of_containers:
    temp = state_of_containers[k].pop()
    top_boxes += temp
print(top_boxes)

"""
--- Part Two ---
Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

"""

# initilize the stack dictionary
stacks_made = {}
# read datafile line by line
with open("/Users/fleigh/Projects/AdventofCode/DecFifth/Map.txt") as f:
    for line in f:
        stack_dict = parse_stack_layer(line, stacks_made)

# once inital state is parse the stack dict needs to be sorted
state_of_containers = OrderedDict(sorted(stack_dict.items()))

# read datafile line by line
with open("/Users/fleigh/Projects/AdventofCode/Dec_5/Instructions.txt") as f:
    for line in f:
        arrange_supply_stacks(line, state_of_containers, "9001")

# now identify the containers at the top of every stack
# initlizae the return stirng
top_boxes = ''
# itterate through the stacks collecting the top box of each
for k in state_of_containers:
    temp = state_of_containers[k].pop()
    top_boxes += temp
print(top_boxes)
