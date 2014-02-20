myd = {}

for a in range(2, 101):
	for b in range(2, 101):
		c = a**b
		print c, "\n"
		if not myd.has_key(c):
			myd[c] = True
		#print a**b
print len(myd)
