function isPrime(x){
	if (x <= 1) return false;
	for (var i = 2; i <= Math.sqrt(x); i++){
		if (x % i === 0) return false;
	}
	return true;
}

function nextPrime(x){
	for (var i = x+1; i < x*2; i++){
		if (isPrime(i)){
			return i;
		}
	}
}

function isPandigital(x){
	var x_str = '' + x;
	var digits = "1234567890";
	for (var i = 0; i < x_str.length; i++){
		if (x_str.indexOf(digits[i]) < 0)
			return false;
	}
	return true;
}

function isSubStringDivisible(x){
	var x_str = '' + x;
	var nprime = 2;
	var nindex = 1;
	var nlength = 3;
	for (nindex = 1; nindex + nlength <= x_str.length; nindex++){
		var y_str = x_str.substr(nindex, nlength);
		var y = parseInt(y_str);
		if (y % nprime != 0) return false;
		nprime = nextPrime(nprime);
	}
	return true;
}

function main(){
	var sum = 0;
	for (var i = 1023456789; i < 9876543210; i++){
		if (isPandigital(i) && isSubStringDivisible(i)){
			console.log(i);
			sum += i;
		}
			
	}
	console.log("sum:",sum);
}

main();