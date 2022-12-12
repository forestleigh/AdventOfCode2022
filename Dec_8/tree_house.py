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


def is_visible(current: int, neighbors: List, matrix): # helper function to confirm if tree is visible from outside grove
    directions = [True, True, True, True]

    # check current visiblity of tree
    for i, el in enumerate(neighbors):

        # if it is out of range, skip it
        if (is_valid(el[0], el[1]) == False):
            return True

        neighbor_height = matrix[el[0]][el[1]]

        if neighbor_height >= current:
            directions[i] = False

    # base case: if all directions have a tree that blocks view, the tree is not visible
    if all(item is False for item in directions):
        return False

    # else increment neighbors
    next_neighbors: List = []
    for i, el in enumerate(neighbors):
        neighbor_row: int = el[0] + nRow[i]
        neighbor_col: int = el[1] + nCol[i]
        neighbors.append([neighbor_row, neighbor_col])

    # and recursively call this function until a coordinate is invalid
    is_visible(current, next_neighbors, matrix)



def DFS_traversal(row: int, col: int, matrix):  # DFS traversal function to visit every tree once
    global nRow, nCol, visited
    visible_tree_count = 0

    # initialize a stack of pairs
    stack: List = []
    stack.append([row, col])

    while (len(stack) > 0):
        curr: List = stack.pop()
        row: int = curr[0]
        col: int = curr[1]
        curr_height = matrix[curr[0]][curr[1]]

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
        if (is_visible(curr_height, neighbors, matrix) == True):
            visible_tree_count += 1

        # add current to visited
        visited[row][col] = True

    return visible_tree_count

# function call
print(DFS_traversal(0, 0, puzzle))
