"""
--- Day 2: Rock Paper Scissors ---
What would your total score be if everything goes exactly according to your strategy guide?

"""
# re-lable the variables for readability
secret_code_1 = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}
# define game outcomes
outcomes_1 = {
    ("Rock", "Rock"): "draw",
    ("Rock", "Paper"): "win",
    ("Rock", "Scissors"): "lose",
    ("Paper", "Rock"): "lose",
    ("Paper", "Paper"): "draw",
    ("Paper", "Scissors"): "win",
    ("Scissors", "Rock"): "win",
    ("Scissors", "Paper"): "lose",
    ("Scissors", "Scissors"): "draw",
}
# make tables for scoring points
score_outcomes = {"lose": 0, "win": 6, "draw": 3}
score_plays = {"Rock": 1, "Paper": 2, "Scissors": 3}


def expected_RPS_score(gameplay: str):
    """Calculates the expected score for multiple rounds of rock paper scissors. We know the plays of the enemy player and current player and need to calcualte the outcomes
    Args:
        gameplay (str) : a string of two encoded chars describing a single game of RPS
    Returns:
        int: total score for current player against enemy player
    """

    # decode the enemy and current plays to Rock/paper/scisscors
    enemy_play = secret_code_1[gameplay[0]]
    curr_play = secret_code_1[gameplay[2]]
    # look up the outcome of each game in the outcomes dict
    curr_outcome = outcomes_1[(enemy_play, curr_play)]
    # increase the score by the points from outscomes and plays
    score = score_outcomes[curr_outcome] + score_plays[curr_play]

    return score

sum_scores_code_1 = 0
# open the file in a way that automatically closes it
with open("/Users/fleigh/Projects/AdventofCode/Dec_2/Data.txt") as f:
    # reading the data from the file one line at a time
    for line in f:
        sum_scores_code_1 += expected_RPS_score(line)

print(sum_scores_code_1)

"""
--- Part Two ---
Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

"""

# re-lable the variables for readability
secret_code_2 = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}
# define game outcomes
outcomes_2 = {
    ("Rock", "draw"): "Rock",
    ("Rock", "win"): "Paper",
    ("Rock", "lose"): "Scissors",
    ("Paper", "lose"): "Rock",
    ("Paper", "draw"): "Paper",
    ("Paper", "win"): "Scissors",
    ("Scissors", "win"): "Rock",
    ("Scissors", "lose"): "Paper",
    ("Scissors", "draw"): "Scissors",
}

def expected_RPS_score_2(gameplay: str):
    """Calculates the expected score for multiple rounds of rock paper scissors. We know the plays of the enemy player and the outcome of each game and need to cacluate the curent player's plays
    Args:
        gameplay (str) : a string of two encoded chars describing a single game of RPS
    Returns:
        int: total score for current player against enemy player
    """

    # decode the enemy play and the outcome for each game into common english
    enemy_play = secret_code_2[gameplay[0]]
    curr_outcome = secret_code_2[gameplay[2]]
    # look up the current player's play in the outcomes dict
    curr_play = outcomes_2[(enemy_play, curr_outcome)]
    # increase the score by the points from outscomes and plays
    score = score_outcomes[curr_outcome] + score_plays[curr_play]

    return score

sum_scores_code_2 = 0
# opening the file in a way that automatically closes it
with open("/Users/fleigh/Projects/AdventofCode/Dec_2/Data.txt") as f:
    # reading the data from the file one line at a time
    for line in f:
        sum_scores_code_2 += expected_RPS_score_2(line)

print(sum_scores_code_2)
