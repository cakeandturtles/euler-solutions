#include <iostream>
using namespace std;

bool isMult3or5(int x){
  if (x%3==0 or x%5==0){
    return true;
  }
  else{ return false; }
}

int main(){
  int mySum=0;
  for(int i=0; i<1000; i++){
    if (isMult3or5(i)){
      mySum+=i;
    }
  }

  cout << mySum << "\n";
  return 0;
}
