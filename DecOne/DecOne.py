# opening the file in a way that automatically closes it
with open("/Users/fleigh/Projects/AdventofCode/DecOne/DecOne.txt", "r") as f:
  # reading the data from the file
  file_data = f.read()
  # splitting the file data into a list with attention for empty lines
  lines = file_data.splitlines()

def maxCals(list):
    # initialize elf counter and cache
    curr = 1
    elf_dict = {}

    # iterate through the list
    for i in list:
        # when empty space, increment current elf
        if i == '':
            curr += 1
        # otherwise, add to that elf's calorie sum
        else:
            elf_dict[curr] = elf_dict.get(curr, 0) + int(i)

    # convert dict into list of tuples sorted by the calorie values
    sorted_elves_by_cals = sorted(
        elf_dict.items(), key=lambda x: x[1], reverse=True)

    # return a list of the results 
    return sorted_elves_by_cals[0:3]

#check work
print(maxCals(lines))
