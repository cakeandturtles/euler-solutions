#include <iostream>
#include <math.h>
using namespace std;

int HowManyFactors(int num)
{
  int j=0;
  for (int i=1; i<=(int) sqrt((double) num); i++)
  {
    if (num%i==0)
      j+=1;
  }
  return j*2;
}

int main()
{
  int currNum=1;
  int triangleNum=currNum;
  while (HowManyFactors(triangleNum)<=500)
  {
    currNum+=1;
    triangleNum+=currNum;
  }
  cout << triangleNum << endl;
  return 0;
}
