from common import *

def indexed_search(id, db, index):
	ratings, raters = get_info(db, id)
	songs = {}
	for rater in raters:
		score1 = db[id]['ratings'][rater]
		for song, score in index[rater].items():
			if song == id: continue
			if song in songs:
				songs[song].append((score1, score))
			else:
				songs[song] = [(score1, score)]
	top3 = sorted([(get_score(scores), song) for song, scores in songs.items()])[:3]
	#print top3
	return [result[1] for result in top3]


if __name__ == '__main__':
	try: input_file = open('../queries.txt')
	except IOError: input_file = create_queries(int(argv[1]), int(argv[2]))
	process(
		berkdb.open('../dbs/asn4_db', 'r'), 
		input_file, 
		open('../output/indexedanswers.txt', 'w'),
		indexed_search,
		berkdb.open('../dbs/asn4_index', 'r'))