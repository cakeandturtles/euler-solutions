#Problem 1: Add all the natural numbers below one thousand that are multiples of 3 or 5

def isMult3or5(x):
  if (x%3==0 or x%5==0):
    return True
  else: return False

mySum=0
for i in range(1000):
  if (isMult3or5(i)):
    mySum+=i

print "The sum is:",mySum
