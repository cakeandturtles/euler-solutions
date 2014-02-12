def uniqueDigits(x):
	strX = str(x)
	uniqueStrX = ''.join(set(strX))
	if len(strX) == len(uniqueStrX):
		return True
	return False

def pandigitalNine(p, m, d):
	strPMD = str(p) + str(m) + str(d)
	strPMD = ''.join(sorted(strPMD))
	if strPMD == "123456789":
		return True
	return False




def main():
	mySum = 0
	for i in xrange(1000, 9876+1):
		if uniqueDigits(i):
			minDivisor = i
			for j in xrange(2, i/2):
				if j >= minDivisor: break
				if i % j == 0:
					if not uniqueDigits(j): continue
					if pandigitalNine(i, j, i/j):
						mySum += i
						break
					if (i/j) < minDivisor:
						minDivisor = i/j

	print mySum



main()

