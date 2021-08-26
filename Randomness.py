import string
from random import randint, choice

def randomness(length):
	final_string = ""

	for number in range(0, length):
		number = number # A completely pointless line
		possible_character_string = string.ascii_letters + "0123456789*~%#$"
		final_string += choice(possible_character_string)

	return final_string

print(randomness(16))
