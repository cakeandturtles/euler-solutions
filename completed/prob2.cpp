#include <iostream>
using namespace std;

int main(){
  int mySum=0;
  int i=1;
  int j=2;
  while (i<4000000){
    if (j%2==0){ mySum+=j; }
    j+=i;
    i=j-i;
  }
  cout << mySum << endl;
  return 0;
}
