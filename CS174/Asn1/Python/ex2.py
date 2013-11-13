

DIF = -32

while 1:
		orig = input('Please enter a four character string: ')
		if len(orig) != 4: print('Sorry, string must be four characters.')
		else: break

conv = ''.join([chr(ord(c) + DIF) for c in orig])
print('The string capitalized is', conv)