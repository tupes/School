

NUM_BITS = 8

while 1:
		bits = input('Please enter an eight digit binary number: ')
		if len(bits) != NUM_BITS:
			print('Sorry, number must be', str(NUM_BITS), 'digits.')
		elif bits.count('0') + bits.count('1') != NUM_BITS:
			print('Sorry, number must be in binary.')
		else: break

binList = reversed(list(bits))
total = sum([2 ** exp for exp in range(NUM_BITS) if binList[exp] == '1'])
print('The decimal equivalent of ' + bits + ' is ' + str(total) + '.')

