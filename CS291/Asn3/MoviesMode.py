
from Mode import *

class MoviesMode(Mode):
    def __init__(self, curs, name):
        self.query = ('''
            select media.id, media.title, rating
            from buy
            join media on (buy.mediaid = media.id)
            join movie on (buy.mediaid = movie.mid)
            left outer join rate on (buy.username = rate.username and buy.mediaid = rate.movieid)
            where
              buy.username = ''' + "'"+name+"'")
        
        self.prompt = "Enter 'rate' followed by the movie ID and your rating, or anything else to return to the main menu: "
        self.commands = {'rate': self.rate}
        Mode.start(self, curs, name, 3)

    def format(self, title, mid, rating):
        return title + ' (ID '+ mid +') Rating: ' + rating
    
    def rate(self, values):
        self.process(values, self.validate, self.insert)
    
    def validate(self, values):
        if values[0] not in self.cache:
            print '\n', 'Sorry, rating must be for a movie you own'
            return False
        try:
            mid = int(values[0])
            rating = int(values[1])
        except ValueError:
            print '\n', 'Sorry, Movie ID and rating must be integers'
            return False
        if not 0 <= rating <= 10:
            print '\n', 'Sorry, rating must be between 0 and 10'
            return False
        return mid, rating

    def insert(self, values):
        self.curs.execute("insert into rate values('"+self.name+"',"+str(values[0])
            +","+str(values[1])+")")

    def success(self, values):
        print '\n', 'Rating for ' + str(values[0]) + ' has been added'

    def double(self, values):
        self.update(values[0], values[1])
        print '\n', 'Rating for ' + str(values[0]) + ' has been updated'

    def update(self, movieID, rating):
        self.curs.execute('''
            update Rate
            set rating = :new_rating
            where
                username = :name and movieID = :mid''',
            new_rating = rating, name = self.name, mid = movieID)