#Problem 3: What is the largest prime factor of the number 600851475143

def isPrime(x):
  i=2
  while i<=int(round(x/2)):
    if (x%i==0): return False
    i+=1
  return True

def primeFactors(num):
  listOfPF=[] #creates an empty list which will be used to hold the prime factors
  while (num%2==0): #this chunk of code takes care of all 2s that may be prime factors
    num/=2
    listOfPF.append(2)

  i=3 #the first nonEven primeNumber
  while num!=1:
    while (num%i==0): #while instead of if in order to account for multiple identical prime factors
      if (isPrime(i)):
        num/=i
        listOfPF.append(i) 
    i+=2 #increment by 2 because all the powers of 2 were taken care of by chunk above

  return listOfPF

def main(): print primeFactors(600851475143)

