import sys

SEPARATOR = '=' * 60
WIDTH = 20

class Animal(object):
	def __init__(self, id):
		self.id = id
		self.stations = [0, 0]
	
	def recordVisit(self, station):
		number = int(station.name[-1]) - 1
		self.stations[number] += 1


class Station(object):
	def __init__(self, name):
		self.name = name
		self.months = [0] * 12
	
	def recordVisit(self, month):
		self.months[month - 1] += 1
	
	def calculateAvg(self):
		self.average = int(sum(self.months) / 12)
	
	def getMaxMonth(self):
		self.maxVisits = max(self.months)
		for m in range(11, -1, -1):
			if self.months[m] == self.maxVisits:
				self.maxMonth = str(m + 1)
				if len(self.maxMonth) == 1: self.maxMonth = '0' + self.maxMonth
				break
	

def getData():
	fileName = sys.argv[1]
	f = open(fileName)
	lines = f.readlines()
	f.close()
	return lines

def parseData(lines, animals, stations):
	for line in lines:
		(animal_id, month, station_name) = parseLine(line)
		if animal_id not in animals:
			animals[animal_id] = Animal(animal_id)
		if station_name not in stations:
			stations[station_name] = Station(station_name)
		recordVisit(animals[animal_id], stations[station_name], month)

def parseLine(line):
	line = line.rstrip()
	chunks = line.split(':')
	return (chunks[0], int(chunks[1][:2]), chunks[2])

def recordVisit(animal, station, month):
	animal.recordVisit(station)
	station.recordVisit(month)

def bothStationAnimals(animals):
	matches = []
	for id in animals:
		if min(animals[id].stations) >= 4:
			matches.append(id)
	return matches

def calculateStats(stations):
	for name in stations:
		stations[name].calculateAvg()
		stations[name].getMaxMonth()

def print_line(*cols):
	for col in cols:
		col = str(col)
		chars = len(col)
		print(col + (' ' * (WIDTH - chars)), end='')
	print('')

def output1(animals):
	print('Number of times each animal visited each station:')
	print_line('Animal Id', 'Station 1', 'Station 2')
	ids = sorted(list(animals.keys()))
	for id in ids:
		animal = animals[id]
		print_line(id, animal.stations[0], animal.stations[1])

def output2(animals, ids):
	print(SEPARATOR)
	print('Animals that visited both stations at least 4 times:')
	ids.sort()
	for id in ids:
		print(id)

def output3(stations):
	print(SEPARATOR)
	print('Average of the number visits in each month for each station:')
	print_line('Station 1', 'Station 2')
	print_line(stations['s1'].average, stations['s2'].average)

def output4(stations):
	print(SEPARATOR)
	print('Month with the maximum number of visits for each station:')
	print_line('Station', 'Month', 'Number')
	print_line(1, stations['s1'].maxMonth, stations['s1'].maxVisits)
	print_line(2, stations['s2'].maxMonth, stations['s2'].maxVisits)

lines = getData()
animals = {}
stations = {}
parseData(lines, animals, stations)
answer2 = bothStationAnimals(animals)
calculateStats(stations)

output1(animals)
output2(animals, answer2)
output3(stations)
output4(stations)