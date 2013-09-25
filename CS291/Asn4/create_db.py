from sys import argv
import shelve as berkdb

def create_db(db, index, file):
	for record in file.read().split('{')[1:]:
		id, title, artists, ratings = parse(record)
		store_in_db(db, id, title, artists, ratings)
		store_in_index(index, id, ratings)
	for f in (db, index, file): f.close()

def parse(record):
	parts = [part[: part.find(']')].strip() for part in record.split('[')]
	ratings = {rating[: rating.find(',')].strip() : int(rating[rating.find(',')+1 : rating.find(')')])
		for rating in parts[4].split('(')[1:]}
	return parts[1], parts[2], parts[3], ratings

def store_in_db(db, id, title, artists, ratings):
	db[id] = {'title': title, 'artists': artists, 'ratings': ratings}

def store_in_index(db, id, ratings):
	for user, score in ratings.items():
		if user in db:
			db[user][id] = score
		else:
			db[user] = {id: score}
	

if __name__ == '__main__':
	create_db(
		berkdb.open('../dbs/asn4_db', 'n'), 
		berkdb.open('../dbs/asn4_index', 'n', writeback=True),
		open('../data/'+argv[1]))
	