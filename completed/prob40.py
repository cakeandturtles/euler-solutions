str_frac = ""
str_frac_len = 0
last_int = 0

def d(n):
	global str_frac
	global str_frac_len
	global last_int
	while (str_frac_len < n):
		last_int += 1
		str_frac += str(last_int)
		str_frac_len += len(str(last_int))
	return int(str_frac[n-1])



def main():
	result = 1
	i = 1
	while (i <= 1000000):
		result *= d(i)
		i *= 10
	print result

main()
