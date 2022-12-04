"""
--- Day 1: Calorie Counting ---
Santa's reindeer typically eat regular reindeer food, but they need a lot of magical energy to deliver presents on Christmas. For that, their favorite snack is a special type of star fruit that only grows deep in the jungle. The Elves have brought you on their annual expedition to the grove where the fruit grows.
To supply enough magical energy, the expedition needs to retrieve a minimum of fifty stars by December 25th. Although the Elves assure you that the grove has plenty of fruit, you decide to grab any fruit you see along the way, just in case.
Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).
The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

To begin, get your puzzle input.

--- Part One ---

"""
#solution below is )(n) in time complexity and space complexity
#if I had not tracked the elf ids it could have had better space compleity

# opening the file in a way that automatically closes it
with open("/Users/fleigh/Projects/AdventofCode/DecOne/DecOne.txt", "r") as f:
  # reading the data from the file
  file_data = f.read()
  # splitting the file data into a list with inclusion of empty lines
  cals_list_by_elf = file_data.splitlines()

# we will keep track of both the cals and which elves have the cals 
def maxCals(cals_list):
    # initialize elf counter and cache
    curr_elf_id = 1
    elf_dict = {}
    max_cals= 0

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
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.
To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

"""
#this solution in O(nlogn) in time compleity due to the addition of sorting 
#still order n space complexity 

# opening the file in a way that automatically closes it
with open("/Users/fleigh/Projects/AdventofCode/DecOne/DecOne.txt", "r") as f:
  # reading the data from the file
  file_data = f.read()
  # splitting the file data into a list with inclusion of empty lines
  cals_list_by_elf = file_data.splitlines()

# we will keep track of both the cals and which elves have the cals 
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
