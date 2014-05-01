function triangle(n){ return n*(n+1)*0.5; }
function pentagon(n){ return n*(3*n-1)*0.5; }
function  hexagon(n){ return n*(2*n-1); }

function main(){
	tri_n = 285; pen_n = 165; hex_n = 143;
	tri_n++; 	//Increment tri_n so we can begin searching for the next equal combo
	tri = triangle(tri_n);
	pen = pentagon(pen_n);
	hex = hexagon(hex_n);
	
	while (!(tri === pen && pen === hex)){
		if (tri >= pen && tri >= hex){		//Triangle is current largest
			if (pen < hex){ pen_n++; pen = pentagon(pen_n); }
			else{ hex_n++; hex = hexagon(hex_n); } 
		}
		else if (pen >= tri && pen >= hex){ 	//Pentagon is current largest
			if (tri < hex){ tri_n++; tri = triangle(tri_n); }
			else{ hex_n++; hex = hexagon(hex_n); }
		}
		else if (hex >= tri && hex >= pen){	//Hexagon is current largest
			if (tri < pen){ tri_n++; tri = triangle(tri_n); }
			else{ pen_n++; pen = pentagon(pen_n); }
		}
	}
	console.log(tri);
}

main();