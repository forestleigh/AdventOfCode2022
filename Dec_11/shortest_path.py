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

visited: Set = set() # List for visited nodes
queue: List = [] # Initialize a queue

#function for Bredth First Search
def bfs(visited, matrix, start):
  visited.add(start)
  queue.append(start)
  step_count = 0

  while queue:
    point = queue.pop(0)
    current_location = matrix[point.y][point.x]
    # print ('current location: ', current_location)

    # define four points
    top = Point(point[0], point[1] + 1)
    bottom = Point(point[0], point[1] - 1)
    left = Point(point[0] - 1, point[1])
    right = Point(point[0] + 1, point[1])
    neighbors = [top, bottom, left, right]

    for neighbor in neighbors:
        try:
            # if the step is one or less up from the current step (rule)
            if matrix[neighbor.y][neighbor.x] <= current_location + 1 \
                and not neighbor.y < 0 and not neighbor.x < 0 \
                and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        except IndexError:
            pass
    step_count += 1

  return step_count

# function calling
print(bfs(visited, puzzle, start_point))
print('visitied: ', len(visited))
# print('step count: ', step_count)

