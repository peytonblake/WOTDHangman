from wotd import *


def printList(l):
    for i in range(len(l)):
        print(l[i] + " ", end="")
    print("")


def loser(solution, guess):
    print("YOU LOST!")
    print("Your guess: ", end="")
    printList(guess)
    print("Solution:   ", end="")
    printList(solution)


def printBoard(guess, misses, guesses):
    clear()
    if misses == 0:
        print("  ________")
        print("  |      |")
        print("         |")
        print("         |")
        print("         |")
        print("         |")
        print("         |")
        print("          ")
    elif misses == 1:
        print("  ________")
        print("  |      |")
        print("  O      |")
        print("         |")
        print("         |")
        print("         |")
        print("         |")
        print("          ")
    elif misses == 2:
        print("  ________")
        print("  |      |")
        print("  O      |")
        print("  |      |")
        print("  |      |")
        print("         |")
        print("         |")
        print("          ")
    elif misses == 3:
        print("  ________")
        print("  |      |")
        print("  O      |")
        print("  |/     |")
        print("  |      |")
        print("         |")
        print("         |")
        print("          ")
    elif misses == 4:
        print("  ________")
        print("  |      |")
        print("  O      |")
        print(" \\|/     |")
        print("  |      |")
        print("         |")
        print("         |")
        print("          ")
    elif misses == 5:
        print("  ________")
        print("  |      |")
        print("  O      |")
        print(" \\|/     |")
        print("  |      |")
        print(" /       |")
        print("         |")
        print("          ")
    elif misses == 6:
        print("  ________")
        print("  |      |")
        print("  O      |")
        print(" \\|/     |")
        print("  |      |")
        print(" /\\      |")
        print("         |")
        print("          ")

    if misses != 0:
        print("You have guessed: ", end="")
        printList(guesses)
    printList(guess)


def playAgain():
    response = input("Would you like to play again? (y/n)")
    if response.lower() == "y":
        return True
    return False


def hangman(word):
    solution = list(word)
    guess = ["_"] * len(solution)
    guesses = []
    misses = 0
    playing = True

    while playing:
        printBoard(guess, misses, guesses)
        guessing = True
        letter = input("Make a guess:").lower()

        while guessing:
            if letter in guesses:
                print("You have already guessed that letter, try again!")
                letter = input("Make a guess:").lower()
            elif not letter.isalpha():
                print("That was not a letter, please stick to the alphabet")
                letter = input("Make a guess:").lower()
            else:
                guesses.append(letter)
                guessing = False

        if letter not in solution:
            misses += 1
            if misses == 6:
                printBoard(guess, misses, guesses)
                loser(solution, guess)
                playing = False

        else:
            correctIndex = [index for (index, item) in enumerate(
                solution) if item == letter]
            for i in correctIndex:
                guess[i] = letter

        if "_" not in guess:
            printBoard(guess, misses, guesses)
            print("You guessed it, you win!!")
            playing = False


if __name__ == "__main__":
    word = getWord().lower()
    hangman(word)
    while playAgain():
        hangman(word)
