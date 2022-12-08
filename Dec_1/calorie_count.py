"""
--- Day 1: Calorie Counting ---
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

"""
# solution below is )(n) in time complexity and space complexity
# if I had not tracked the elf ids it could have had better space compleity

# opening the file in a way that automatically closes it
with open("/Users/fleigh/Projects/AdventofCode/DecOne/Data.txt", "r") as f:
  # reading the data from the file
  file_data = f.read()
  # splitting the file data into a list with inclusion of empty lines
  cals_list_by_elf = file_data.splitlines()

# we will keep track of both the cals and which elves have the cals


def maxCals(cals_list):
    # initialize elf counter and cache
    curr_elf_id = 1
    elf_dict = {}
    max_cals = 0

    # iterate through the list
    for i in cals_list:
        # when empty space, increment current elf id
        if i == '':
            curr_elf_id += 1
        # otherwise, add to that elf's calorie sum in the elf dict (gotta convert the type to int)
        else:
            elf_dict[curr_elf_id] = elf_dict.get(curr_elf_id, 0) + int(i)
            # and check if this elf has the max cals so far
            max_cals = max(max_cals, elf_dict[curr_elf_id])

    # identify which elf/elves has the value matching our max cals count
    elf_with_max_cals = [k for k, m in elf_dict.items() if m == max_cals]

    # return the elf id and calorie amount
    return (elf_with_max_cals, max_cals)


# call function and print to terminal
print(maxCals(cals_list_by_elf))


"""
--- Part Two ---
Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

"""
# this solution in O(nlogn) in time compleity due to the addition of sorting
# still order n space complexity

# opening the file in a way that automatically closes it
with open("/Users/fleigh/Projects/AdventofCode/DecOne/Data.txt", "r") as f:
  # reading the data from the file
  file_data = f.read()
  # splitting the file data into a list with inclusion of empty lines
  cals_list_by_elf = file_data.splitlines()

# we will keep track of both the cals AND which elves have the cals

def maxCals2(cals_list):
    # initialize elf counter and cache
    curr_elf_id = 1
    elf_dict = {}

    # iterate through the list
    for i in cals_list:
        # when empty space, increment current elf id
        if i == '':
            curr_elf_id += 1
        # otherwise, add to that elf's calorie sum (gotta convert the type to int)
        else:
            elf_dict[curr_elf_id] = elf_dict.get(curr_elf_id, 0) + int(i)

    # convert dict into list of tuples sorted by the calorie values
    sorted_elves_by_cals = sorted(
        elf_dict.items(), key=lambda x: x[1], reverse=True)

    # return array of 3 tuples containing the 3 elf ids (i=0) amd the largest calorie amounts (i=1)
    top_three_elves = sorted_elves_by_cals[0:3]

    # calculate sum of cals for the 3 elves
    sum_cals_top_three = 0
    for elf in top_three_elves:
        sum_cals_top_three += elf[1]

    # return the top 3 elves and the sum of their cals
    return top_three_elves, sum_cals_top_three


# call function and print to terminal
print(maxCals2(cals_list_by_elf))
