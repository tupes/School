

sizes = [36, 12, 1]
CM_IN_INCHES = 2.54

# I tried to write a general greedy algorithm that would
# work for both questions 5 and 6, and possible future work
def greedy(total, sizes, isDiscrete):
		quants = []
		for size in sizes[:-1]:
			amount = int(total / size)
			quants.append(amount)
			total -= amount * size
		total = round(total, 2)
		if isDiscrete:
			quants.append(int(total / sizes[-1]))
		else:
			quants.append(total / sizes[-1])
		return quants

while 1:
		try:
			cm = float(input('How many centimeters do you want to convert? '))
			break
		except ValueError:
			print('Sorry, please enter a number.')

inches = cm / CM_IN_INCHES
quants = greedy(inches, sizes, False)
print('This is', quants[0], 'yards,', quants[1], 'feet,', quants[2], 'inches.')