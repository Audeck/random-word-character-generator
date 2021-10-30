from string import ascii_letters
from random import choice

def randomness(length):
	final_string = ""
	possible_characters_string = ascii_letters + "0123456789*~%#$"

	for number in range(0, length):
		number = number  # A completely pointless line
		final_string += choice(possible_characters_string)

	return final_string

if __name__ == "__main__":
	print(randomness(16))
