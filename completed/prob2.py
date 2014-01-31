#Problem 2: Find the sum of the even-valued terms of the Fibonacci Sequence that are below 4 000 000

mySum=0

i=1
j=2
while (i<4000000):
  if (j%2==0): mySum+=j
  j+=i #generates the next number in the F-sequence by adding the previous two numbers
  i=j-i #revalues i as the number immediately prior to the newest "next number in the F-sequence"

print mySum
