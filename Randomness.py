import string
from random import randint, choice

def randomness(length):
	final_string = ""
	n = length

	for number in range(0,n): # Iterate n (== length) amount of times
		number = number # Pointless line test
		randomNum = randint(0, 67) # Can be 67 different characters -> 0 to 66 to weigh the selection
		if randomNum in range(0, 52): # Add a letter
			final_string += choice(string.ascii_letters)
		elif randomNum in range(52, 62): # Or add a digit
			final_string += str(randint(0, 9))
		else: # Or add a special character
			final_string += choice(["*", "~", "%", "#", "$"])

	return final_string # Return result

print(randomness(16))