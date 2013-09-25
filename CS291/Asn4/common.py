import shelve as berkdb
from math import sqrt
from random import choice
from time import clock

def process(db, input_file, output_file, search_func, index=None):
	times = []
	for line in input_file:
		start = clock()
		id = line.strip()
		output(output_file, id, search_func(id, db, index))
		times.append(clock() - start)
	times.sort()
	total = sum(times)
	print 'Total querying time:', total, 'secs (average:', total/float(len(times)), 'secs/query). Fastest query:', times[0], 'secs. Slowest query:', times[-1], 'secs.'

def get_info(db, id):
	ratings = db[id]['ratings']
	raters = set(ratings.keys())
	return ratings, raters

def get_score(matches):
	return sqrt(sum([(match[0] - match[1]) ** 2 for match in matches])) / float(len(matches))

def output(file, id, answers):
	file.write(', '.join([id] + [str(answer) for answer in answers]) + '\n')

def create_queries(num_queries, max_song):
	f = open('../queries.txt', 'w')
	for x in range(num_queries): f.write(str(choice(range(max_song)))+'\n')
	f.close()
	return open('../queries.txt')