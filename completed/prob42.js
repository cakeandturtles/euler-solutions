var fs = require('fs');
var path = require('path');

function readTextFile(filename){
	var file_path = path.join(__dirname + '\\' + filename);
	return { text: fs.readFileSync(file_path, 'utf-8'), index: 0 };
}

function getNextWord(file){
	/*this only works specific to the structure of words.txt*/
	file.index++;
	var token = "";
	while (file.text[file.index] !== ',' && file.index < file.text.length){
		token += file.text[file.index];
		file.index++;
	}
	if (file.index === file.text.length) "";
	file.index++;
	return token.substring(0, token.length-1);
}

function checkTriangularity(word, triangles){
	var value = 0;
	var abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	for (var i = 0; i < word.length; i++){
		var chr = word[i];
		value += (abc.indexOf(chr)+1);
	}

	return isTriangleNum(value);
}

function isTriangleNum(value){
	var triangle = 1;
	var n = 1;
	while (triangle < value){
		n++;
		triangle = 0.5*n*(n+1);
	}
	if (triangle === value) return true;

	return false;
}

var main = function(){
	var file = readTextFile("../bin/words.txt");

	var count = 0;
	var word = getNextWord(file);
	while (word !== ""){
		//console.log(word);
		if (checkTriangularity(word.toUpperCase())){
			count++;
		}
		word = getNextWord(file);
	}
	console.log("# Triangle Words: " + count);
};

main();
