#include <iostream>
using namespace std;

void convertArrayToLastTen(int array[], unsigned long long num){
	int reverse[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	int count = 0;
	while (num > 0 && count < 10){
		reverse[count] = num % 10;
		num = num / 10;
		count++;
	}
	for (int i = 0; i < 10; i++){
		array[i] = reverse[9-i];
	}
}

unsigned long long convertNumFromArray(int array[]){
	unsigned long long num = 0ULL;
	for (int i = 0; i < 10; i++){
		unsigned long long power = 1ULL;
		for (int j = 0; j < i; j++){
			power *= 10;
		}
		num += array[9-i]*power;
	}
	return num;
}

int printArray(int array[]){
	for (int i = 9; i >= 0; i--){
		cout << array[9-i];
	}
	cout << endl;
}

int main(){
	int n = 1000;

	int sum[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	for (int i = 1; i <= n; i++){
		int power[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		convertArrayToLastTen(power, i);
		for (int j = 2; j <= i; j++){
			unsigned long long temp = convertNumFromArray(power);
			temp *= i;
			convertArrayToLastTen(power, temp);
		}
		unsigned long long temp = convertNumFromArray(sum);
		unsigned long long temp2 = convertNumFromArray(power);
		unsigned long long newSum = temp + temp2;
//		cout << "newSum: " << newSum << endl;
		convertArrayToLastTen(sum, newSum);

//		cout << "I: " << i << endl;
//		cout << "Pow: ";
//		printArray(power);
//		cout << "Sum: ";
//		printArray(sum);
//		cout << "Press Enter to continue... ";
//		cin.ignore();
	}
	printArray(sum);
	return 0;
}
