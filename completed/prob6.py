#Problem 6: Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum

i=1
sumSquare=0
squareSum=0

while i<=100:
  sumSquare+=i**2
  squareSum+=i
  i+=1

squareSum=squareSum**2

print (squareSum-sumSquare)
