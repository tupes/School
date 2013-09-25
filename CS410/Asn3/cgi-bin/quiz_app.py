#!/usr/bin/env python

from cgi import FieldStorage
from os import environ
import html

class AppCGI(object):
	header = 'Content-Type: text/html\n\n'
	html = '''
	<html>
		<head>
			<title>410 Asn3</title>
		</head>
		<body>
			%s
		</body>
	</html>
'''
	cookies = dict()
	
	def getCookies(self):
		if 'HTTP_COOKIE' not in environ:
			self.cookies['user'] = self.cookies['info'] = ''
			return
		cookies = [x.strip() for x in environ['HTTP_COOKIE'].split(';')]
		for cookie in cookies:
			pass # TO DO
	
	def setCookies(self):
		for cookie in self.cookies:
			print 'Set-Cookie: %s=%s; path=/' % (cookie, quote(self.cookies[cookie]))
	
	def show(self):
		print AppCGI.header + AppCGI.html % self.html

	def run(self):
		self.show()


if __name__ == '__main__':
	app = AppCGI()
	app.run()