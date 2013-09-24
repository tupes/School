
sizes = [20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
names = ['twenties', 'tens', 'fives', 'ones', 'quarters', 'dimes', 'nickels', 'pennies']

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
		cost = float(input('How much did the item cost: '))
		rec = float(input('How much did the person give you: '))
		break
	except ValueError:
		print('Sorry, please enter only numbers.')

if cost > rec:
		print('Sorry, the person did not give you enough.')
else:
		change = rec - cost
		quants = greedy(change, sizes, True)
		output = zip(quants, names)
		print("The person's change is $" + str(change))
		print('The bills or the change should be:')
		for num, name in output:
			print(num, name)