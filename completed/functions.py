import math

def isPrime(x):
  i=2
  while i<=int(round(math.sqrt(x))):
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

def factors(num):
  listOfF=[] #creates an empty list which will be used to hold all the factors
  i=1
  while (i<=int(round(math.sqrt(num)))):
    if (num%i==0):
      listOfF.append(i)
    i+=1
  return listOfF

def howManyFactors(num):
  i=1
  howMany=0
  while (i<=int(round(math.sqrt(num)))):
    if (num%i==0):
      howMany+=1
    i+=1
  return howMany
