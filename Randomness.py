from string import ascii_letters
from random import choice

def randomness(length):
	final_string = ""
	possible_character_string = ascii_letters + "0123456789*~%#$"

	for number in range(0, length):
		number = number # A completely pointless line
		final_string += choice(possible_character_string)

	return final_string

print(randomness(16))
