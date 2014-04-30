def isPandigital(res):
	d = '0123456789'
	for i in range(0, len(d)):
		count = 0
		for j in range(0, len(res)):
			if d[i] == res[j]: count += 1
		if count > 1 or (count > 0 and i == 0): return False
	return True



def main():
	pandigital = 0
	for i in xrange(9, 9999):
		temp = 2
		res = str(i)
		ispandigital = True
		while (len(res) < 9 and ispandigital):
			res += str(i*temp)
			temp += 1
			ispandigital = isPandigital(res)

		if len(res) == 9 and ispandigital:
			iRes = int(res)
			if iRes > pandigital: 
				pandigital = iRes
				print "Pandigital: " + res
	print "Highest: " + str(pandigital)
	

main()
