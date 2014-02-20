#include <iostream>
#include <math.h>

using namespace std;

unsigned long int recursive
         (unsigned long int i, int r, int d, int n)
{
  if (r==n || d==n)
    return ++i;
  else
  {
    i = recursive(i, r+1, d, n);
    i = recursive(i, r, d+1, n);
    return i;
  }
}

int main()
{
  unsigned long int i;
  int n;
  cout << "n = ";
  cin >> n;
  i = recursive(0, 0, 0, n);
  cout << i << endl;
  return 0;
}
