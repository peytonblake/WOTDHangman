from wordOfTheDay import *

def getWord():
	raw_html = simple_get('https://www.merriam-webster.com/word-of-the-day')
	soup = BeautifulSoup(raw_html, 'html.parser')
	title = soup.title.text.split()
	return title[4]

def printList(l):
	for i in range(len(l)):
		print(l[i] + " ", end="")
	print("")

def loser(solution, guess):
	print("YOU LOST!")
	print("Your guess: ", end="")
	printList(guess)
	print("Solution: ", end="")
	printList(solution)

def printBoard(solution, guess, misses):
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

	printList(guess)

def hangman(wotd):
	solution = list(wotd)
	guess = ["_"] * len(solution)
	misses = 0
	playing = True

	while playing:
		printBoard(solution, guess, misses)
		letter = input("Make a guess:")

		if letter not in solution:
			misses += 1
			if misses == 6:
				printBoard(solution, guess, misses)
				loser(solution, guess)
				playing = False

		else:
			correctIndex = [index for (index, item) in enumerate(solution) if item == letter]
			for i in correctIndex:
				guess[i] = letter

		if "_" not in guess:
			print("You guessed it, you win!!")
			playing = False


if __name__ == "__main__":
	wotd = getWord().lower()
	hangman(wotd)