with open("/Users/fleigh/Projects/AdventofCode/Dec_8/Data.txt") as f:
    data = f.read().splitlines()

# initiate the puzzle matrix
puzzle = []
for el in data:
    row = list(el)
    puzzle.append([int(num) for num in row])

print(puzzle)

# example of how to iterate through a matrix with indexes in a pythonic fashion
def print_matrix (matrix): 
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            print(element, i, j)

# print(print_matrix(puzzle))

def find_visible_trees (matrix):
    result = []

    for i, row in enumerate(matrix):
        for j, element in enumerate(row):

            # initialize conditions
            try:
                compare_above = element > matrix[i][j-1]
            except IndexError:
                compare_above = True
            try:
                compare_below = element > matrix[i][j+1]
            except IndexError:
                compare_below = True
            try:
                compare_left = element > matrix[i-1][j]
            except IndexError:
                compare_left = True
            try:
                compare_right = element > matrix[i+1][j]
            except IndexError:
                compare_right = True

            if compare_above and compare_below and compare_left and compare_right:
                result.append(element)

    return result

print(find_visible_trees(puzzle))
