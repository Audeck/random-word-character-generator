#Naming the file random.py might not have been my brightest idea

import string
from random import randint, choice

final_string = ""
count = while count < 16:
	if randint(0,1) == 0:
		final_string += choice(string.ascii_letters)
	else:
		final_string += str(randint(0,9))
	count += 1

print(final_string)
