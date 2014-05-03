function isRightTriangle(a,b,c){
	return ((a*a)+(b*b) === (c*c));
}

function main(){
	var p = 3 + 4 + 5;
	var max_p = p;
	var max_num_sol = 1;

	while (p <= 1000){
		var num_sol = 0;
		for (var c = 5; c < p/2; c++){
			for (var b = 4; b <= c-1; b++){
				for (var a = p-c-b; a <= b-1; a++){
					//console.log(p, a, b, c);
					if (a+b+c === p && isRightTriangle(a,b,c)){
						num_sol++;
					}
				}
			}
		}
		if (num_sol > max_num_sol){
			console.log(p, num_sol);
			max_p = p;
			max_num_sol = num_sol;
		}
		p++;
	}
	console.log("p: ", max_p, ", # solutions: ", max_num_sol);
}

main();
