#!/usr/bin/env python

from json import load
from random import sample
from quiz_app import AppCGI

class Quiz(AppCGI):
	data_path = 'data.json'
	html = '''
		<p id="timer">Timer: <span id="examElapsed">0</span> Seconds.</p>
		<p id="questionTimer0">Question 1 Timer: <span id="questionElapsed0">0</span> Seconds.</p>
		<p id="questionTimer1">Question 2 Timer: <span id="questionElapsed1">0</span> Seconds.</p>
		<p id="questionTimer2">Question 3 Timer: <span id="questionElapsed2">0</span> Seconds.</p>
		<p id="questionNumber">Question: <span id="question">1</span> / 3</p>
		<p id="progress">Progress: <span id="answered">0</span> / 3</p>
		
		<div id="container">
			<div id="progress-bar">
			</div>
		</div>
		
		<p>Directions: Closed book, no talking, and one hour.</p>
		
		<form id='buttons' action="/cgi-bin/results.py">
			<input type="button" id="prev" value="prev">
			<input type="button" id="next" value="next">
			<input type="submit" id="submit" value="submit">
			<input type="hidden" name="timer" value=0>
		</form>
'''

	def get_questions(self, num):
		questions = [load(line) for line in open(self.data_path)]
		self.questions = sample(questions, len(questions))

	def store_results(self):
		pass


if __name__ == '__main__':
	app = Quiz()
	app.run()