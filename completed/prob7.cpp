#include <iostream>
using namespace std;

bool isPrime(long long x)
{
  bool returnVal=true;
  for (long long i=x/2; i>1; i--)
  {
    if (x%i==0)
      returnVal=false;
  }
  return returnVal;
}

int main()
{
  long long myPrime=3;
  long long i;

  for (int count=2; count!=10001; count++)
  {
    cout << myPrime << "\t" << count << "\n";
    i=myPrime+2;
    while (not isPrime(i))
      i+=2;
    myPrime=i;
  }
  cout << myPrime << "\n";
  return 0;
}
