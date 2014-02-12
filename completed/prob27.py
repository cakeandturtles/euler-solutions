import math

primes = {}

def isPrime(x):
	if primes.has_key(x): return primes[x]

	i=2
	while i<=int(round(math.sqrt(x))):
		if (x%i==0): 
			primes[x] = False
			return False
		i+=1
	primes[x] = True
	return True


def main():
	nmax = 0
	amax = 0
	bmax = 0
	for a in xrange(-999,1000):
		for b in xrange(-999, 1000):
			n = 0
			nres = math.pow(n, 2) + (a * n) + b
			while nres > 1 and isPrime(nres):
				n += 1
				nres = math.pow(n, 2) + (a * n) + b
			if n > nmax:
				nmax = n
				amax = a
				bmax = b
	print nmax, amax, bmax, amax * bmax

main()
