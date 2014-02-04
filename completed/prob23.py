import sys
import math

abundantNum = {}

def isAbundant(x):
	if abundantNum.has_key(x): return abundantNum[x]

	mySum = 0
	for i in range(1, x/2+1):
		if x % i == 0:
			mySum += i
	if mySum > x: 
		abundantNum[x] = True
		return True
	abundantNum[x] = False
	return False
	

def isSumOfTwoAbundant(x):
	for i in range(2, x):
		if isAbundant(i) and isAbundant(x-i):
			return True
	return False

def prob23():
	mySum = 1 + 2 + 3;
	sys.stdout.write("Working")
	for i in range (4, 28124):
		if i % 1000 == 0: sys.stdout.write(".")
		if not isSumOfTwoAbundant(i):
			mySum += i
	print
	print mySum

	
prob23()
