
// VALIDATION FUNCTIONS
function validate(evt) {
	var res1 = validateName();
	var res2 = validatePostalCode();
	var res3 = validateEmail();
	var res4 = validateBirthDate();
	if (res1 && res2 && res3 && res4) {
		createCookie(get('username'));
		return true;
	}
	evt.preventDefault();
}

function validateName() {
	if (get('username') === "") {
		alert("Must provide a Name");
		return false;
	}
	return true;
}

// currently works for any 6 char permutation of letters and numbers
function validatePostalCode() {
	var input = get('postalCode');
	if (input == "") return true;
	if (input.length != 6) {
		alert("Postal Code must be in LNLNLN format");
		return false;
	}
	var output = "";
	var x;
	for (var k = 0; k < input.length; k++) {
		x = input.substring(k, k+1);
		if (isLetter(x) || isNumber(x)) {
			output += x;
		}
	}
	if (input != output) {
		alert("Postal Code must be in LNLNLN format");
		return false;
	}
	return true;
}

function validateEmail() {
	var input = get('email');
	if (input == "") {
		alert("Must provide an email address");
		return false;
	}
	var output = "";
	// tiny finite state machine
	var foundAt = false;
	var foundDot = false;
	var suffixLength = 0;
	var lookingFor = 'char';
	for (var k = 0; k < input.length; k++) {
		x = input.substring(k, k+1);
		if (!isValid(x)) {
			alert("Email address contains spaces or invalid characters");
			return false;
		}
		
		if (lookingFor == 'char') {
			if (x == '@') {
				alert("Email address must contain characters before '@'");
				return false;
			}
			else if (x == '.') {
				alert("Email address must contain characters between '@' and '.'");
				return false;
			}
			else if (foundDot)
				suffixLength += 1;
			else if (foundAt)
				lookingFor = '.';
			else
				lookingFor = '@';
		}
			
		else if (lookingFor == '@' && x == '@') {
			foundAt = true;
			lookingFor = 'char';
		}
		
		else if (lookingFor == '.') {
			if (x == '@') {
				alert("Email address must contain only one '@'");
				return false;
			}
			else if (x == '.') {
				foundDot = true;
				lookingFor = 'char';
			}
		}
	}
	// finished scanning string
	if (!foundAt)	{
		alert("Email address must contain '@'");
		return false;
	}
	else if (!foundDot) {
		alert("Email address must contain '.'");
		return false;
	}
	else if (suffixLength < 2) {
		alert("Email address must contain at least 2 characters after '.'");
		return false;
	}
	else return true;
}

// currently works for any separator character, not just / or -
function validateBirthDate() {
	var x = get('birthDate');
	if (x == "") return true;
	if (x.length != 10) {
		alert("Birth Date must be in DD/MM/YYYY or YYYY/MM/DD format");
		return false;
	}
	if (allNumbers(x, [0, 1, 3, 4, 6, 7, 8, 9]) || allNumbers(x, [0, 1, 2, 3, 5, 6, 8, 9])) {
		return true;
	}
	alert("Birth Date must be in DD/MM/YYYY or YYYY/MM/DD format");
	return false;
}

// COOKIE FUNCTION (modified from http://www.quirksmode.org/js/cookies.html)
function createCookie(value) {
	var date = new Date();
	date.setTime(date.getTime() + (24*60*60*1000));
	var expires = '; expires=' + date.toGMTString();
	var info = 'username=' + value + expires;
	document.cookie = info;
}

// UTILITY FUNCTIONS
function get(attr) {
	return document.signUp[attr].value;
}

function isLetter(x) {
	return (x >= "A" && x <= "Z") || (x >= "a" && x <= "z");
}

function isNumber(x) {
	return (x >= "0") && (x <= "9");
}

function allNumbers(string, indices) {
	for (var i = 0; i < indices.length; i++) {
		if (!(isNumber(string.substring(indices[i], indices[i+1])))) return false;
	}
	return true;
}

function isValid(x) {
	return isLetter(x) || isNumber(x) || ['@', '.', '[', ']', '_', '-'].indexOf(x) > -1;
}

// CREATE EVENT LISTENER
document.getElementById("signUp").addEventListener('submit', validate);


