

while 1:
		try:
			amount = float(input('What is the amount of US Dollars you wish to convert? '))
			rate = float(input('What is the current exchange rate\n(1~US Dollar equals what in the Foreign Currency)? '))
			break
		except ValueError:
			print('Sorry, please enter only numbers.')

curr = round(amount * rate, 2)
print('The amount in the Foreign Currency is $%.2f' % curr)