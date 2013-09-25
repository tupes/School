from sys import argv
from common import *

def linear_search(id, db, index=None):
	ratings1, raters1 = get_info(db, id)
	top3 = [(float('inf'), None), (float('inf'), None), (float('inf'), None)]
	for key in db:
		if key == id: continue
		ratings2, raters2 = get_info(db, key)
		matches = {(ratings1[rater], ratings2[rater]) for rater in raters1 & raters2}
		if not matches: continue
		top3 = sorted(top3 + [(get_score(matches), key)])[:3]
	#print 'final top 3 are:', top3
	return [result[1] for result in top3]

if __name__ == '__main__':
	try: input_file = open('../queries.txt')
	except IOError: input_file = create_queries(int(argv[1]), int(argv[2]))
	process(
		berkdb.open('../dbs/asn4_db', 'r'), 
		input_file, 
		open('../output/linearanswers.txt', 'w'),
		linear_search)
