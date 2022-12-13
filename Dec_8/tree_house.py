""" 
--- Day 8: Treetop Tree House ---
How many trees are visible from outside the grove? 
"""

from typing import List

with open("/Users/fleigh/Projects/AdventofCode/Dec_8/Data.txt") as f:
    data = f.read().splitlines()

# initiate the puzzle matrix and size variables
puzzle: List = []
for el in data:
    row = list(el)
    puzzle.append([int(num) for num in row])


def print_matrix(matrix):  # practice traversing a matrix
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            print(element, i, j)
# print(print_matrix(puzzle))


# Initialize direction vectors
nRow: List = [0, 1, 0, -1]
nCol: List = [-1, 0, 1, 0]
ROW_MAX: int = len(puzzle[0])
COL_MAX: int = len(puzzle)
visited: List = [[False for i in range(ROW_MAX)] for j in range(COL_MAX)]


def is_valid(row:int, col:int):  # helper function to confirm if a coordinate is in-bounds
    global ROW_MAX, COL_MAX, visited

    # if cell is out of bounds
    if (row < 0 or col < 0 or row >= ROW_MAX or col >= COL_MAX):
        return False

    # otherwise, it is valid
    return True

def is_visited(row:int, col:int):  # helper function to confirm if a coordinate is unvisited
    global ROW_MAX, COL_MAX, visited

    # if the cell is already visited
    if (visited[row][col]):
        return False

    # otherwise, it can be visited
    return True


def is_visible(current: List, neighbors: List, matrix, directions, at_boundary): # helper function to confirm if tree is visible from outside grove
     # default is the tree is visible (directions=[True, True, True, True])
     # default is the neighbor is not on the boundary (at_boundary=[False, False, False, False)

    curr_height = matrix[current[0]][current[1]]

    # check current visiblity of tree
    for i, el in enumerate(neighbors):

        # if it is out of range its at the boundary
        if (is_valid(el[0], el[1]) == False):
            at_boundary[i] = True
            continue

        neighbor_height = matrix[el[0]][el[1]]

        # if the neighbor is taller then it blocks the current tree from that direction
        if neighbor_height >= curr_height:
            directions[i] = False

    # base case: if all directions have a tree that blocks view, the tree is not visible
    if all(item is False for item in directions):
        return False

    # base case: if all directions have found the boundary and function is still going, the tree is visible
    if all(item is True for item in at_boundary):
        return True

    # else increment neighbors
    # neighbors example [[3,2], [4,3], [3, 4], [2, 3]]
    next_neighbors = neighbors
    next_neighbors[0][1] -= 1 # send north more north
    next_neighbors[1][0] += 1 # send east more east
    next_neighbors[2][1] += 1 # send south more south
    next_neighbors[3][0] -= 1 # send west more west

    # and recursively call this function until a coordinate is invalid
    is_visible(current, next_neighbors, matrix, directions, at_boundary)



def DFS_traversal(row: int, col: int, matrix):  # DFS traversal function to visit every tree once
    global nRow, nCol, visited
    visible_tree_count = 0
    tree_visited_count = 0

    # initialize a stack of pairs
    stack: List = []
    stack.append([row, col])

    while (len(stack) > 0):
        curr: List = stack.pop()
        row: int = curr[0]
        col: int = curr[1]

        # check if current is valid or not
        if (is_valid(row, col) == False):
            continue # skip

        # check if current is visited or not
        if (is_visited(row, col) == False):
            continue # skip

        # set neighbors back to empty
        neighbors: List = []

        # collect neighbors in stack and neighbors array
        for i in range(4):
            neighbor_row: int = row + nRow[i]
            neighbor_col: int = col + nCol[i]
            # neighbor_height = matrix[neighbor_row][neighbor_col]
            stack.append([neighbor_row, neighbor_col])
            neighbors.append([neighbor_row, neighbor_col])

        # check if tree is visible
        directions = [True, True, True, True]
        at_boundary = [False, False, False, False]
        if (is_visible(curr, neighbors, matrix ,directions, at_boundary) == True):
            visible_tree_count += 1

        # add current to visited
        visited[row][col] = True
        tree_visited_count += 1

    return 'visible trees:', visible_tree_count,'trees visited: ', tree_visited_count

# function call
print(DFS_traversal(0, 0, puzzle))
