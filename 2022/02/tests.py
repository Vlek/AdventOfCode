from enum import Enum
import pytest


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


@pytest.mark.parametrize(
    "x,y,score",
    [
        (GameChoices.Rock, GameChoices.Rock, 4),
        (GameChoices.Rock, GameChoices.Paper, 1),
        (GameChoices.Rock, GameChoices.Scissors, 7),
        (GameChoices.Paper, GameChoices.Rock, 8),
        (GameChoices.Paper, GameChoices.Paper, 5),
        (GameChoices.Paper, GameChoices.Scissors, 2),
        (GameChoices.Scissors, GameChoices.Rock, 3),
        (GameChoices.Scissors, GameChoices.Paper, 9),
        (GameChoices.Scissors, GameChoices.Scissors, 6),
    ],
)
def test_calc(x: GameChoices, y: GameChoices, score: int) -> None:
    assert calcRoundScore(x, y) == score
