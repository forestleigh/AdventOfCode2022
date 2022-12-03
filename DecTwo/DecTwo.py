"""
--- Day 2: Rock Paper Scissors ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: 
A for Rock, 
B for Paper, and 
C for Scissors. 

The second column--" Suddenly, the Elf is called away to help with someone's tent. The second column, you reason, must be what you should play in response: 
X for Rock, 
Y for Paper, and 
Z for Scissors. 

Winning every time would be suspicious, so the responses must have been carefully chosen. The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. 

The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.
For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?

"""
# opening the file in a way that automatically closes it
with open("/Users/fleigh/Projects/AdventofCode/DecTwo/DecTwo.txt", "r") as f:
  # reading the data from the file
  file_data = f.read()
  # splitting the file data into a list by new lines and by spaces
  lines = file_data.split()

#define function that calculates the total score and accepts array as argument
def expectedScore (list):

    # edge case: if array length is odd return false
    if (len(list) % 2 != 0):
        return False

    # initilize the scores for plays
    plays = {
        "A" : 1, "X" : 1,
        "B" : 2, "Y" : 2,
        "C" : 3, "Z" : 3
    }

    # initilize score varaible
    score = 0

    # iterate list every other item starting at index 1
    for index, el in enumerate(list):
        # only check the even indexes so that odd indexs = index + 1
        if index % 2 == 0 and index != len(list) - 1:

            # check for a draw first (+3 points)
            if plays[el] == plays[list[index + 1]]:
                score += 3
                # add points for the play type
                score += plays[el]

            # now check for wins (+6 points)
            # check if opponent played losing value
            # [A, X], [B, Y], [C, Z] = ["Rock", "Rock"], ["Paper", "Paper"], ["Scissors", "Scissors"]
            elif [list[index + 1], el] == ["Y", "A"] or [list[index + 1], el] == ["Z", "B"] or [list[index + 1], el] == ["X", "C"]:
                score += 6
                # add points for the play type
                score += plays[list[index + 1]]

            # now check for losses (+0 points)
            else:
                # add points for the play type
                score += plays[list[index + 1]]

    return score

print(expectedScore(lines))


"""
--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

"""

# opening the file in a way that automatically closes it
with open("/Users/fleigh/Projects/AdventofCode/DecTwo/DecTwo.txt", "r") as f:
  # reading the data from the file
  file_data = f.read()
  # splitting the file data into a list by new lines and by spaces
  lines = file_data.split()

#define function that calculates the total score and accepts array as argument
def expectedScore2 (list):

    # edge case: if array length is odd return false
    if (len(list) % 2 != 0):
        return False

    # initilize the rules (key > value)
    rules = {
        "A" : "C",
        "B" : "A",
        "C" : "B"
    }

    # initilize the scores for plays
    plays = {
        "A" : 1,
        "B" : 2,
        "C" : 3,
    }

    # Use desctructuring to define the code for plays (makes equality possible for draws)
    [ A, B, C ] = [ "Rock", "Paper", "Scissors" ]

    # initilize score varaible
    score = 0

    # iterate list every other item starting at index 1
    for index, el in enumerate(list):
        # only check the even indexes so that odd indexs = index + 1
        if index % 2 == 0 and index != len(list) - 1:

            # check for a draw first (+3 points)
            if list[index + 1] == "Y":
                score += 3
                # add points for the play type
                score += plays[el]

            # now check for losses (+0 points)
            elif list[index + 1] == "X":
                # check find the losing value (look up value by key in rules)
                v = rules[el]
                # add points for the play type
                score += plays[v]

            # now check for wins (X) (+6 points)
            else:
                score += 6
                # check find the winning value (look up key by value in rules)
                v = [k for k, m in rules.items() if m == el]
                # add points for the play type
                score += plays[v[0]]

    return score

print(expectedScore2(lines))