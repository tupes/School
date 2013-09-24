

while 1:
		try:
			miles = float(input('Please enter the miles you drove: '))
			gallons = float(input('Please enter the gallons of gas you put in the tank: '))
			break
		except ValueError:
			print('Sorry, please only enter numbers.')

mpg = miles / gallons
print('You got', mpg, 'mpg on that tank of gas.')