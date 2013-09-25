#!/usr/bin/env python

from quiz_app import AppCGI

class Results(AppCGI):
	html = '''
		<h2>Results for <span id='username2'></span>:</h2>
		Q1: correct, <span id="q1Time"></span> seconds<br>
		Q2: correct, <span id="q2Time"></span> seconds<br>
		Q3: incorrect, <span id="q3Time"></span> seconds<br>
		Total Score: 66%<br>
		Time Taken: <span id="examTime"></span> seconds
'''


if __name__ == '__main__':
	app = Results()
	app.run()