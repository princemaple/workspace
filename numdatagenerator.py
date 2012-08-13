# random number generator

from random import choice, randint
from itertools import permutations as per

lines = raw_input("how many lines of input>> ")
if not lines: exit()
lines = int(lines.strip())

f = open("test_data", "w")

init = 0
while init < lines:
	f.write(str(randint(0, lines)) + "\n")
	init += 1

print "%d lines random data done" % lines

f.close()

raw_input()