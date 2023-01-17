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


def calcRoundScore(PlayerChoice: GameChoices, OpponentChoice: GameChoices) -> int:
    """
    Returns sum of points granted by choices made.
    """
    # Regardless of outcome, we get the points for our choice.
    result: int = PlayerChoice.value

    num_choies: int = len(GameChoices)

    # Draw
    if OpponentChoice == PlayerChoice:
        result += GameOutcomes.Draw.value
    # We win
    #
    # Because we have already taken care of the
    # Note, our logic here is very similar to what you'd use for a caesar
    # cypher. What we are going to do is use modulo to loop back around if the
    # number is larger than our collection size. In this case, it's only ever
    # going to be one larger than the collection, but it keeps our logic nice
    # and neat.
    elif wins_against[PlayerChoice] == OpponentChoice:
        result += GameOutcomes.Win.value
    # Note, no opponent win condition. We do not get points anyway.

    return result


# This is the collective scores of all of the rounds of rock paper scissors
# that will be played using the strategy guide that was proposed.
round_scores: list[int] = []


with open("2_input.txt", "r") as game_data:

    for line in game_data:

        # Each line will come in as a pair of choices, e.g. A Y
        # With Python, you also need to strip away the newline characters.
        #
        # What we're going to do is split them so that we have two choices, one
        # from our opponent and then the one that we're supposed to make.
        game: list[str] = line.strip().split()

        opponents_choice: GameChoices = notation_to_choices[game[0]]
        our_choice: GameChoices = notation_to_choices[game[1]]

        round_scores.append(calcRoundScore(our_choice, opponents_choice))


print(
    f"The total score received for following the given strategy is: {sum(round_scores)}"
)
