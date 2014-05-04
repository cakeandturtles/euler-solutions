function isPrime(x){
	for (var i = 2; i < Math.sqrt(x); i++){
		if (x % i === 0) return false;
	}
	return true;
}

function isPandigital(x){
	var x_str = '' + x;
	var digits = "123456789";
	for (var i = 0; i < x_str.length; i++){
		if (x_str.indexOf(digits[i]) < 0)
			return false;
	}
	return true;
}

function main(){
	var largest = 2143;
	for (var i = 100000000; i < 1000000000; i++){
		if (isPandigital(i) && isPrime(i)){
			largest = i;
		}
		if (i % 10000)
		console.log(i);
	}
	console.log("Largest pandigital prime:",largest);
}

main();
