"""
--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

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
with open("/Users/fleigh/Projects/AdventofCode/DecFifth/Map.txt") as f:
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
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.
Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.
The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.
Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

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
with open("/Users/fleigh/Projects/AdventofCode/DecFifth/Instructions.txt") as f:
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
