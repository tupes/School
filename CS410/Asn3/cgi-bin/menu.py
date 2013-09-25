#!/usr/bin/env python

from quiz_app import AppCGI

class Menu(AppCGI):
	html = '''
		<h2>Welcome! Would you like to:</h2>
		<form action="/cgi-bin/quiz.py">
			<input type="submit" value="Take Quiz">
		</form>
		<form action="/cgi-bin/admin.py">
			<input type="submit" value="Admin Module">
		</form>
'''



if __name__ == '__main__':
	app = Menu()
	app.run()