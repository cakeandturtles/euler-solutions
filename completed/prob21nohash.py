def d(n):
	dsum = 0
	for i in range(n/2, 0, -1):
		if n % i == 0:
			dsum += i
	return dsum


def main():
	ddsum = 0
	for i in range(2, 10000):
		if i % 100 == 0: print "Loading...",i
		dsum = d(i)

		if i != dsum:
			dsum2 = d(dsum)
			if dsum2 == i:
				ddsum += i

	print "Complete!\n"
	print "Sum: ",ddsum

main()
