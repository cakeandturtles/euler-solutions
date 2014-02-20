import itertools
import sys

def prob24():
	millionthPer = list(itertools.permutations("0123456789"))[999999]
	for i in range(0, 10):
		sys.stdout.write(millionthPer[i])

prob24()
