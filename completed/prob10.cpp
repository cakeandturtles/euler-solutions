#include <iostream>
#include <math.h>

using namespace std;

bool isPrime(long x)
{
  if (x%3==0 or x%5==0 or x%7==0 or x%11==0 or x%13==0)
    return false; 
  for (long n = (int) sqrt(x); n>1; n--)
  {
    if (x%n==0)
      return false;
  }
  return true;
}

int main()
{
  long currPrime=3;
  long i;
  unsigned long long mySum=2;
  
  while (currPrime<2000000)
  {
    mySum+=currPrime;
    cout <<"Current Prime: "<<currPrime<<" Current Sum: "<<mySum<<endl;
    i=currPrime+2;
    while (not isPrime(i))
      i+=2;
    currPrime=i;
  }
  cout << mySum << "\n";
  return 0;
}
