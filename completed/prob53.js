function exc(x){
	if (x === 0 || x === 1) return 1;
	else return (x * exc(x-1));
}

function C(n, r){
	if (r > n) return 0;
	else{
		var result = exc(n);
		result /= exc(r);
		result /= exc(n-r);
		return result;
	}
}

function main(){
	var count = 0;
	for (var n = 23; n <= 100; n++){
		for (var r = 1; r < n; r++){
			if (C(n, r) > 1000000){
				count++;
			}
		}
	}
	console.log(count);
}

main();
