function sameDigits(x, y){
	var x_str = "" + x;
	var y_str = "" + y;
	if (x_str.length != y_str.length) return false;
	for (var i = 0; i < x_str.length; i++){
		var index = y_str.indexOf(x_str[i]);
		if (index < 0 || index != y_str.lastIndexOf(x_str[i]))
			return false;
	}
	return true;
}

function main(){
	var i = 1;
	while (!(sameDigits(i, 2*i) && sameDigits(i, 3*i) && sameDigits(i, 4*i) && sameDigits(i, 5*i) && sameDigits(i, 6*i))){
		i++;
	}
	console.log(i);
}

main();
