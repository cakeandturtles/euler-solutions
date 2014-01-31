#include <iostream>
using namespace std;

unsigned long long calcDiagonals(int N){
	if (N % 2 == 0) return 0ULL;
	if (N == 1) return 1ULL;
	else{
		unsigned long long sum = 1ULL, cnt = 1ULL, inc = 2ULL;
		while (N > 1){
			for (int i = 0; i < 4; i++){
				cnt += inc;
				sum += cnt;
			}
			inc += 2;
			N -= 2;
		}
		return sum;
	}
}

int main(){
	int N = 1;
	while (N <= 1001){
		cout << "N: " << N << ", diagonal: " << calcDiagonals(N) << endl;
		N+=2;
		if ((N-1) % 50 == 0){
			cout << "Press enter to continue..";
			cin.ignore();
		}
	}
}
