from wotd import *


def printWordle(word, guess):
    for letter in guess:
        print(letter, end="")
    print()

    for i in range(len(word)):
        if guess[i] == word[i]:
            print("O", end="")
        elif guess[i] in word:
            print("L", end="")
        else:
            print("X", end="")
    print()


def wordle(word):
    guessCount = 0

    for letter in word:
        print("_", end="")
    print()

    while guessCount < 6:
        guessing = True
        guess = input("Make a guess:").lower()
        while guessing:
            if len(guess) != len(word):
                print("Guess must be same length as WOTD, try again!")
                guess = input("Make a guess:").lower()
            elif not guess.isalpha():
                print("Guess must contain only letters, try again!")
            else:
                printWordle(word, guess)
                if guess == word:
                    print("You guessed it, you win!!")
                    return
                else:
                    guessCount += 1
                    guessing = False


if __name__ == "__main__":
    word = getWord().lower()
    wordle(word)
    while playAgain():
        wordle(word)
