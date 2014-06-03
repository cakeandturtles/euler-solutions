function readFile(filename){
	fs = require('fs')
	fs.readFile(filename, 'utf8', function (err,data) {
	if (err) {
		return console.log(err);
	}
	return data;
	});
}

function find(pcodes, d){
	var index = {x: -1, y: -1};
	if (pcodes === []) return index;
	else{
		for (var i = 0; i < pcodes.length; i++){
			index.x = i;
			for (var j = 0; j < pcodes[i].length; i++){
				if (pcodes[i][j]===d){
					index.y = j;
					return index;
				}
			}
		}
		index.x = -1;
		return index;
	}
}

function solve(data){
	var pcodes = [];
	for (var i = 0; i < data.length; i++){
		for (var j = 0; j < data[i].length; j++){
			var new_code = [];
			//working on each digit in a specific successful attempt sequence
			var count = 0;
			var index = find(pcodes, data[i][j]);
			if (index.x === -1){
				
			}
		}
	}
}

function main(){
	var data = readFile("../bin/keylog.txt").split("\n");
	solve(data);
}

main();