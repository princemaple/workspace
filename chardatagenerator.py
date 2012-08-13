# this python file is for generating testing data for
# subject comp20003 algorithm&datastructure project 1
# Po Chen - Student ID: 531943
# Subject: COMP20003 Algorithm and Data Structure

from random import choice, randint
from itertools import permutations as per

lines = raw_input("how many lines of input>> ")
if not lines: exit()
lines = int(lines.strip())

f = open("randomdata", "w")

chars = [chr(c) for c in range(ord('A'), ord('Z')+1)]
# chars += [chr(c) for c in range(ord('a'), ord('z')+1)]

init = 0
while init < lines:
	temp = ""
	for i in xrange(randint(4, 20)):
		temp += choice(chars)
	f.write(temp+"\n")
	init += 1

print "%d lines random data done" % lines

f.close()

f = open("ordereddata", "w")
chars = [chr(c) for c in range(ord('A'), ord('K')+1)]
gene = per( chars )
init = 0
while init < lines:
	f.write("".join(gene.next())+"\n")
	init += 1

print "%d lines ordered data done" % lines

f.close()

raw_input()