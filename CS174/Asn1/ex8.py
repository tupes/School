

while 1:
		try:
			num = int(input('Please enter a number: '))
		except ValueError:
			print('Sorry, that was not a number.')
			continue
		if not 0 <= num <= 255:
			print('Sorry, number must within the range 0-255.')
		else: break

rems = ['0'] * 8
counter = 0
div = num
while div > 0:
		rems[counter] = str(div % 2)
		div = int(div / 2)
		counter += 1

rems.reverse()
rems = ''.join(rems)
print('The binary equivalent of ' + str(num) + ' is ' + rems + '.')
