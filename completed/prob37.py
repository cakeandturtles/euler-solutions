import itertools
import sys
import math

isPDict = dict()

def isPrime(n):
	if n == 1: return False
	for i in xrange(2, int(math.sqrt(n)+1)):
		if n%i==0: return False
	return True

def getAllTruncates(n):
	digits = str(n)
	truncates = []
	for i in range(1, len(digits)):
		truncates.append(digits[i:])
		#print digits[i:]
		truncates.append(digits[:i])
		#print digits[:i]
	return truncates

def isTruncatablePrime(n):
	ps = getAllTruncates(n)
	for i in xrange(0, len(ps)):
		p = ps[i]
		d = 0
		while len(p) > 0:
			dd = int(p[0])
			for i in range(0, len(p)-1):
				dd *= 10
			d += dd
			p = p[1:]
		if d in isPDict:
			if not isPDict[d]: return False
		else:
			isprime = isPrime(d)
			isPDict[d] = isprime
			if not isprime: return False
	print str(n) + " is a truncatabale Prime!"
	return True
	

def solve():
	tnum = 0
	tsum = 0
	i = 23
	while tnum < 11:
		isprime = False
		if i in isPDict:
			isprime = isPDict[i]
		else:
			isprime = isPrime(i)
			isPDict[i] = isprime
		if isprime:
			if isTruncatablePrime(i):
				tnum += 1
				tsum += i
		i+=1
	return tsum


def main():
	print "The sum of 11 truncatable primes is: " + str(solve())

main()

