"""
The Elves begin to set up camp on the beach. To decide whose tent gets to be
closest to the snack storage, a giant Rock Paper Scissors tournament is already
in progress.

Rock Paper Scissors is a game between two players. Each game contains many
rounds; in each round, the players each simultaneously choose one of Rock,
Paper, or Scissors using a hand shape. Then, a winner for that round is
selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats
Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy
guide (your puzzle input) that they say will be sure to help you win. "The
first column is what your opponent is going to play: A for Rock, B for Paper,
and C for Scissors. The second column--" Suddenly, the Elf is called away to
help with someone's tent.

The second column, you reason, must be what you should play in response: X for
Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious,
so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your
total score is the sum of your scores for each round. The score for a single
round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3
for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if
the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you
should calculate the score you would get if you were to follow the strategy
guide.

Second Star:

The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?



Tries:
    6295: Answer was too small.
"""


from enum import Enum


class GameChoices(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


class GameOutcomes(Enum):
    Win = 6
    Draw = 3
    Lose = 0


notation_to_choices: dict[str, GameChoices] = {
    "A": GameChoices.Rock,
    "B": GameChoices.Paper,
    "C": GameChoices.Scissors,
    "X": GameChoices.Rock,
    "Y": GameChoices.Paper,
    "Z": GameChoices.Scissors,
}

wins_against: dict[GameChoices, GameChoices] = {
    GameChoices.Rock: GameChoices.Scissors,
    GameChoices.Scissors: GameChoices.Paper,
    GameChoices.Paper: GameChoices.Rock,
}

result: int = 0

with open("2_input.txt", "r") as game_data:

    for line in game_data:

        # Each line will come in as a pair of choices, e.g. A Y
        # With Python, you also need to strip away the newline characters.
        #
        # What we're going to do is split them so that we have two choices, one
        # from our opponent and then the one that we're supposed to make.
        game: list[str] = line.strip().split()

        opponents_choice: GameChoices = notation_to_choices[game[0]]
        our_choice: GameChoices

        # If we should win,
        if game[1] == "Z":
            result += GameOutcomes.Win.value
            our_choice = wins_against[wins_against[opponents_choice]]
        # If we should draw,
        elif game[1] == "Y":
            result += GameOutcomes.Draw.value
            our_choice = opponents_choice
        # If we should lose,
        else:
            our_choice = wins_against[opponents_choice]

        result += our_choice.value


print(f"The total score received for following the given strategy is: {result}")
