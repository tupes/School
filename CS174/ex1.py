

while 1:
		name = input('Please enter your name: ')
		if len(name) < 4:
			print('Sorry, the name must contain at least four characters.')
		else: break

for c in name[:4]:
		print(c, 'ASCII value is', ord(c))