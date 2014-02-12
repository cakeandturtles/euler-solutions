#include <iostream>
using namespace std;

long long solve(int p, int pp, int fp, int tp, int twp, int ffp, int lb, int max){
	int n = p+(2*pp)+(5*fp)+(10*tp)+(20*twp)+(50*ffp)+(100*lb);
	if (n == max) return 1LL;
	else if (n > max) return 0LL;

	long long ways = 0LL;
	ways += solve(p, pp, fp, tp, twp, ffp, lb+1, max);
	ways += solve(p, pp, fp, tp, twp, ffp+1, lb, max);
	ways += solve(p, pp, fp, tp, twp+1, ffp, lb, max);
	ways += solve(p, pp, fp, tp+1, twp, ffp, lb, max);
	ways += solve(p, pp, fp+1, tp, twp, ffp, lb, max);
	ways += solve(p, pp+1, fp, tp, twp, ffp, lb, max);
	ways += solve(p+1, pp, fp, tp, twp, ffp, lb, max);
	return ways;
}

int main(){
	cout << solve(0, 0, 0, 0, 0, 0, 0, 200) + 1LL << endl;
}
