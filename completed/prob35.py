import itertools
import sys
import math

isPDict = dict()

def isPrime(n):
	for i in xrange(2, int(math.sqrt(n)+1)):
		if n%i==0: return False
	return True

def getAllRotations(n):
	digits = str(n)
	rotations = []
	for i in range(1, len(digits)):
		rotations.append(digits[i:]+digits[:i])
	return rotations

def isCircularPrime(n):
	ps = getAllRotations(n)
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
	print str(n) + " is a circular Prime!"
	return True
	

def solve():
	cpsum = 13
	for i in xrange(100, 1000000):
		isprime = False
		if i in isPDict:
			isprime = isPDict[i]
		else:
			isprime = isPrime(i)
			isPDict[i] = isprime
		if isprime:
			if isCircularPrime(i):
				cpsum += 1
	return cpsum


def main():
	print "There are " + str(solve()) + " circular primes!"

main()

