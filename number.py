import random

secret = random.randint(1,10)


def game():
	guesses = []
	while len(guesses) <5:
			guess = int(input("Guess any number between 1 and 10:"))	
			if guess == secret:
				print("That's The Number dude")
				break

			elif guess > secret:
				print("{} is way to higher than my number".format(guess))

			else:
				print("{} is lower than my number".format(guess))

			guesses.append(guess)

	else:
		print("Oops !! ,you din't get it my number was {}".format(secret))

		choice = input("Do You want to play game again. Y/n")

		if choice.lower() != 'n':
			game()

		else:
			print("You played it well . Thanks for using it , Bye!!")

game()
