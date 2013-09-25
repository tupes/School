
// INIT FUNCTION
function init() {
	window.question = 1;
	window.progress = 0;
	window.times = [0, 0, 0];
	window.answered = [false, false, false];
	window.examStart = new Date().getTime(); 
	window.questionStart = window.examStart;
	hide('P2'); hide('P3'); hide('P4');
	update('username', readCookie());
	update('username2', readCookie());
}

// QUESTION/LISTENER FUNCTIONS
function previousQuestion() {
	if (window.question < 2) return;
	updateQuestionTimer(window.question-1);
	hide('P' + window.question.toString());
	window.question -= 1;
	show('P' + window.question.toString());
	resetQuestionTimer();
	update("question", window.question);
}

function nextQuestion() {
	if (window.question > 2) return;
	updateQuestionTimer(window.question-1);
	hide('P' + window.question.toString());
	window.question += 1;
	show('P' + window.question.toString());
	resetQuestionTimer();
	update("question", window.question);
}

function submitExam() {
	updateQuestionTimer(window.question-1);
	updateResults();
	hide('P' + window.question.toString());
	show('P4');
}

function checkProgress() {
	if (window.answered[window.question-1]) return;
	window.progress += 1;
	window.answered[window.question-1] = true;
	update("answered", window.progress);
	updateBar();
}

// UPDATE HTML FUNCTIONS
function update(id, value) {
	document.getElementById(id).innerHTML = value;
}

function updateExamTimer() {
	var result = getSeconds(window.examStart).toString();
	update('examElapsed', result);
}

function updateQuestionTimer(i) {
	window.times[i] += getSeconds(window.questionStart);
	update('questionElapsed' + i.toString(), window.times[i].toString());
}

function updateResults() {
	update('q1Time', window.times[0].toString());
	update('q2Time', window.times[1].toString());
	update('q3Time', window.times[2].toString());
	update('examTime', getSeconds(window.examStart).toString());
}

function updateBar() {
	var percent = (window.progress / 3) * 100;
	document.getElementById("progress-bar").style.width = percent + '%';
	if (window.progress == 1)
		document.getElementById("progress-bar").style.background = 'red';
	else if (window.progress == 2)
		document.getElementById("progress-bar").style.background = 'yellow';
	else if (window.progress == 3)
		document.getElementById("progress-bar").style.background = 'green';
}

function hide(id) {
	document.getElementById(id).style.display = "none";
}

function show(id) {
	document.getElementById(id).style.display = "inline";
}

// TIMER FUNCTIONS

function resetQuestionTimer() {
	window.questionStart = new Date().getTime(); 
}

function getSeconds(startTime) {
	var seconds = (new Date().getTime() - startTime) / 1000; 
	return seconds;
}

// COOKIE FUNCTION (modified from http://www.quirksmode.org/js/cookies.html)
function readCookie() {
	var name = 'username=';
	var cookies = document.cookie.split(';');
	for (var i = 0; i < cookies.length; i++) {
		var cookie = cookies[i];
		if (cookie.indexOf(name) == 0) 
			return cookie.substring(name.length, cookie.length);
	}
	return 'Unknown User';
}

// create event listeners
document.getElementById('buttons').addEventListener('click', updateExamTimer);
document.getElementById('prev').addEventListener('click', previousQuestion);
document.getElementById('next').addEventListener('click', nextQuestion);
document.getElementById('submit').addEventListener('click', submitExam);
document.getElementById('question1').addEventListener('click', checkProgress);
document.getElementById('question2').addEventListener('click', checkProgress);
document.getElementById('question3').addEventListener('click', checkProgress);

// initialize on load
// these attempts didn't work. reverted to onLoad in html
//init();
//document.onload = init;


