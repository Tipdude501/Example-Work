function coloredLetters() {
	var html = '';

	function randomRGB() {
		return Math.floor(Math.random() * 200);
	}


	function randomColor() {
		var color = "rgb(";
		color += randomRGB() + ',';
		color += randomRGB() + ',';
		color += randomRGB() + ')';
		return color;
	}


	function print(message) {
		document.write(message);
	}

	function changingText() {
		html += '<h1 id="title"><span style="color:' + randomColor() + '">C</span> <span style="color:' + randomColor() + '">O </span> <span style="color:' + randomColor() + '">L</span> <span style="color:' + randomColor() + '">O</span> <span style="color:' + randomColor() + '">R</span> </h1>';
	}		

	changingText();
	print(html);
}


coloredLetters();