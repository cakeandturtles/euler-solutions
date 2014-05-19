#every 3rd term in the fibonacci sequence is even
#x, y, x + y!, x + 2y, 2x + 3y, 3x + 5y! (! means even)
#so in every iteration of the loop, we make x and y the next two odd fibonacci #s,
#and then add the next term (x + y) to the sum
x = y = 1
sum = 0
while (sum < 1000000):
	sum += (x + y)
	x, y = x + 2 * y, 2 * x + 3 * y