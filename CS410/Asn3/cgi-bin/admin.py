#!/usr/bin/env python

from quiz_app import AppCGI

class Admin(AppCGI):
	html = '''
		<h2>What do you want?</h2>
'''



if __name__ == '__main__':
	app = Admin()
	app.run()