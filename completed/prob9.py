#There exists one pythagorean triplet for which a+b+c = 1000, find it.
#NOTE: a<b<c and a^2+b^2=c^2
#NOTE: a, b, and c are positive integers
import math

def recurTrip(a,b):
  if a+b+math.sqrt(a**2+b**2)>1000: return 0
  if math.sqrt(a**2+b**2)%1==0: 
    c=int(math.sqrt(a**2+b**2))
    if a+b+c==1000:
      print a,b,c
      return a*b*c
  return recurTrip(a,b+1)

i=3
temp=recurTrip(i,i+1)
while temp==0:
  i+=1
  temp=recurTrip(i,i+1)
print temp
