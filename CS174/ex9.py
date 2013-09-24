import math

while 1:
		try:
			sideA = float(input('Please enter the length of the first leg: '))
			sideB = float(input('Please enter the length of the second leg: '))
			break
		except ValueError:
			print('Sorry, please enter only numbers.')

hypot = math.sqrt((sideA ** 2) + (sideB ** 2))
print('The length of the hypotenuse is', hypot)
