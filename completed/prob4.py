#Problem 4: Find the largest palindromic number made from the product of two three digit numbers
#A brute force approach :(

def isPalindrome(x):
  x=str(x)
  i=0
  while (i<int(round(len(x)/2))):
    if not (x[i]==x[len(x)-1-i]): return False
    i+=1
  return True

i=999
j=999
maxPalindrome=10000

while (i>99):
  if (isPalindrome(i*j) and i*j>maxPalindrome): maxPalindrome=i*j
  j=999
  while (j>99):
    if (isPalindrome(i*j) and i*j>maxPalindrome): maxPalindrome=i*j
    j-=1
  i-=1

print maxPalindrome
  
