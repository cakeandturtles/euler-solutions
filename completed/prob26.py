def checkRepeat(S):
	n = 4
	L = -1
	for i in xrange(0, len(S)-n):
		splicedS = S[i:]
		#print splicedS
		l = checkSplicedRepeat(splicedS,n)
		if (l > L): L = l
	return L

def checkSplicedRepeat(S, n):
	if len(S) % n == 0 or len(S) < n: return -1
	chunk_size = len(S)/n
	chunks = [S[i:i+chunk_size] for i in range(0, len(S), chunk_size) ]
	if (chunks[0]==chunks[1] and chunks[0]==chunks[2] and chunks[0]==chunks[3]):
		#print chunks
		return len(chunks[0])
	return -1

def main():
	longCycle = 1
	longNum = 1
	for i in xrange(7, 1000):
		print str(i) + "!!!!!!"
		n = 1
		S = ''
		while True:
			n *= 10
			s = n/i
			n -= (i*s)
			if (n == 0): break
			S += str(s)
			l = checkRepeat(S)
			if (l > 0):
				if (l > longCycle): 
					longCycle = l
					longNum = i
				break
	print longNum, longCycle

main()
