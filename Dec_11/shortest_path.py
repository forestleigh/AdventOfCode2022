from typing import List, Dict, Set
import string
from collections import namedtuple

#to prevent x and y from getting mixed up..
Point = namedtuple("Point", ["x", "y"])

# dict to translate chars to heights
char_to_nums: Dict[str,int] = {'S':0, 'E': 25}
for i, char in enumerate(string.ascii_lowercase):
    char_to_nums[char] = i

# initiate the puzzle matrix and start and stop values
with open("/Users/fleigh/Projects/AdventofCode/Dec_11/Data.txt") as f:
    data = f.read().splitlines()
puzzle: List = []
for i,el in enumerate(data):
    row = list(el)
    puzzle.append([char_to_nums[char] for char in row])
    if 'S' in el:
        start_point = Point(x=el.index('S'), y=i)
    if 'E' in el:
        end_point = Point(x=el.index('E'), y=i)
print(puzzle, 'start: ', start_point, 'end: ', end_point)

#function for Bredth First Search
def bfs(matrix, start, end):
    queue: List = [] # Initialize a queue
    queue.append(start)  # push the first path into the queue

    visited: Set = set() # List for visited nodes
    how_many_steps = 0

    while queue:

        new_queue = [] # initilize queue replacement
        for current in queue:

            # initialize current value
            current_elevation = matrix[current.y][current.x]
            
            # if we've made it to the ned return the steps
            if current == end:
                return how_many_steps

            # collect new neighbors in new queue
            elif current not in visited:
                top = Point(current[0], current[1] + 1)
                bottom = Point(current[0], current[1] - 1)
                left = Point(current[0] - 1, current[1])
                right = Point(current[0] + 1, current[1])
                neighbors = [top, bottom, left, right]

                # ensure each neighbor is in bounds
                for neighbor in neighbors:
                    if neighbor.x >= 0 and neighbor.y >= 0:
                        try:
                            # initlize inbound new neighbor values
                            neighbor_value = matrix[neighbor.y][neighbor.x]
                        except IndexError:
                            continue
                        # if the step is one or less up from the current step (rule)
                        if neighbor_value <= current_elevation + 1:
                            # add neighbor to new queue
                            new_queue.append(neighbor)

                # prevent revisiting old neighbors
                visited.add(current)
        
        # increment queue and step count
        queue=new_queue
        how_many_steps += 1

        # address edgecase of end not being found
        if not queue: raise RuntimeError("BFS complete but never found the endpoint - no solution")


# function calling
print(bfs(puzzle, start_point, end_point))

