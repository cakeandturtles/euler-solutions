#include <iostream>
using namespace std;

const int MAX = 200;

unsigned long long solve(){
	unsigned long long ways = 0LL;
	for (int a = 0; a <= 200; a++){
		int A = a*1;
		if (A == 200) ways++; 
		if (A >= 200) break; 
		int bmax = (MAX - A)/2;
		
		for (int b = 0; b <= bmax; b++){
			int B = b*2;
			if (A+B == 200) ways++;
			if (A+B >= 200) break;
			int cmax = (MAX - A - B)/5;

			for (int c = 0; c <= cmax; c++){
				int C = c*5;
				if (A+B+C == 200) ways++;
				if (A+B+C >= 200) break;
				int dmax = (MAX - A - B - C)/10;

				for (int d = 0; d <= dmax; d++){
					int D = d*10;
					if (A+B+C+D == 200) ways++;
					if (A+B+C+D >= 200) break;
					int emax = (MAX - A - B - C - D)/20;

					for (int e = 0; e <= emax; e++){
						int E = e*20;
						if (A+B+C+D+E == 200) ways++;
						if (A+B+C+D+E >= 200) break;
						int fmax = (MAX - A - B - C - D - E)/50;

						for (int f = 0; f <= fmax; f++){
							int F = f*50;
							if (A+B+C+D+E+F == 200) ways++;
							if (A+B+C+D+E+F >= 200) break;
							int gmax = (MAX - A - B - C - D - E - F)/100;
							for (int g = 0; g <= gmax; g++){
								int G = g*100;
								if (A+B+C+D+E+F+G == 200) ways++;
								if (A+B+C+D+E+F+G >= 200) break;
								int hmax = (MAX - A - B - C - D - E - F - G)/200;
								for (int h = 0; h <= hmax; h++){
									int H = h*200;
									if (A+B+C+D+E+F+G+H == 200) ways++;
									if (A+B+C+D+E+F+G+H >= 200) break;
								}
							}
						}
					}
				}
			}
		}
	}
	return ways;
}

int main(){
	cout << solve() << endl;
}
