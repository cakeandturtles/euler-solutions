def d(n):
	dsum = 0
	for i in range(n/2, 0, -1):
		if n % i == 0:
			dsum += i
	return dsum


def main():
	ddsum = 0
	ddict = dict()
	for i in range(2, 10000):
		if i % 100 == 0: print "Loading...",i
		dsum = d(i)
		ddict[i] = dsum	#add number to the ddict

		if i != dsum:
			if dsum in ddict:
				if ddict[dsum] == i:
					ddsum += i
					ddsum += dsum
	print "Complete!\n"
	print "Sum: ",ddsum

main()
