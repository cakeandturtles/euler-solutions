#include <iostream>
using namespace std;

void increment(int* dow){
	(*dow)++;
	if (*dow >= 7)
		*dow = 0;
}

int howManySun(int* dow, int days, int month, int year){
	int sum = 0;
	for (int i = 1; i <= days; i++){
		if (i == 1 && *dow == 0){
			cout << "The day is " << *dow << ", " << month << "/" << i << "/" << year << endl;
			sum++;
		}
		increment(dow);
	}
	return sum;
}


int main(){
	int one = 1;
	int* dow; 
	dow = &one;								//1 Jan 1900 was a Monday

	int sum = 0;

	//Iterate through the years
	for (int i = 1900; i <= 2000; i++){
		if (i == 1901) sum = 0; //Reset sum counter to start at Jan 1, 1901
		//Iterate through the months
		for (int j = 1; j <= 12; j++){
			switch (j){
				case 9: 					//30 days has September
				case 4: case 6: case 11: 	//April, June and November
					sum += howManySun(dow, 30, j, i);
					break;
				case 2: 					//Saving February alone
					if (i % 4 == 0 && (i % 100 != 0 || i % 400 == 0)){
						cout << "It's a leap year! Year: " << i << endl;
						sum += howManySun(dow, 29, j, i);
					}
					else
						sum += howManySun(dow, 28, j, i);
					break;
				default:					//All the rest have 31
					sum += howManySun(dow, 31, j, i);
					break;
			}
		}
	}
	cout << "Sum: " << sum;
	return 0;
}
