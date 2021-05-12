import random
from hangman_ai import *

games_played = 0
wins = 0
wordlist = []

numgames = 10
guesses = 6
verbose = False


def initgame():
    global wordlist

    with open("base_words.txt", "r") as f:
        wordlist = f.read().lower().split("\n")


def gameround():
    global wins, games_played

    word = random.choice(wordlist)
    initword = "_" * len(word)

    initround(initword, wordlist)
    guessed = []
    wrong = 0
    won = False

    while wrong < guesses:
        puzzle = ""
        argument = ""
        correct = 0
        for char in word:
            if char in guessed:
                puzzle += char + " "
                argument += char
                correct += 1
            else:
                argument += "_"
                puzzle += "_ "
        if correct >= len(word):
            won = True
            break

        if verbose:
            print("Your guesses so far: " + str(guessed))
            print("Current Puzzle: " + puzzle)
            print("Remaining Incorrect Guesses:", (guesses - wrong))

        guess = makeguess(argument)
        if guess not in word:
            wrong += 1
        if guess not in guessed:
            guessed.append(guess)

    games_played += 1

    if won:
        wins += 1
        if verbose:
            print("You won the round!")
    else:
        if verbose:
            print("You lost the round. The word was " + word)


def main():
    initgame()

    for _ in range(numgames):
        gameround()

    print("Games Played: ", games_played)
    print("Games Won: ", wins)


if __name__ == "__main__":
    main()
