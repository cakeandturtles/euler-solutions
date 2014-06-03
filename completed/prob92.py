chains = {}

def chainStep(x):
	sum = 0
	while (x > 0):
		temp = x % 10
		sum += temp * temp
		x /= 10
	
	return sum

def chainTo89(x):
	result = False
	addToChains = []
	while (x != 1):
		if (x in chains):
			result = chains[x]
			break
		if (x == 89): 
			result = True
			break
		addToChains.append(x)
		x = chainStep(x)
	for i in range(len(addToChains)):
		chains[addToChains[i]] = result
	return result
		
def main():
	sum = 0
	for i in xrange(1, 9999999):
		if (chainTo89(i)):
			sum += 1
	print sum
	
main()