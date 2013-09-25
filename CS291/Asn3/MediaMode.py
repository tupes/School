
from Mode import *

class MediaMode(Mode):
    def __init__(self, curs, name):
        self.query = "select id, title, price from media"
        self.prompt = ("Enter 'buy' or 'rent' followed by the ID number and its visibility, or anything else to return to the main menu: ")
        self.success_message = 'Transaction successfully processed'       
        self.double_message = 'Sorry, you cannot purchase this item more than once'
        self.commands = {'buy': self.buy, 'rent': self.rent}
        Mode.start(self, curs, name, 3)

    def format(self, title, mid, price):
        return title + ' (ID '+mid+'): $' + price
    
    def buy(self, values):
        price = self.get_price(values[0])
        self.process(list(values) + [price], self.validate, self.insert_buy)

    def rent(self, values):
        fee = self.get_fee(values[0])
        self.process(list(values) + [fee], self.validate_rental, self.insert_rent)

    def validate(self, values):
        if not self.validate_vis(values[1]): return False
        if values[0] not in self.cache:
            print '\n', 'Sorry, invalid ID number'
            return False
        if self.get_credits() < values[2]:
            print '\n', "Sorry, you don't have enough credits"
            return False
        return values
            
    def validate_rental(self, values):
        if self.validate(values):
            if self.get_copies(values[0]) > 0:
                return values
            else:
                print '\n', "Sorry, there are no copies of that movie available"
                self.insert_waiting(values[0])
        return False

    def insert_buy(self, values):
        self.curs.execute('''
            insert into Buy values(:name, :mid, sysdate, :vis)''',
            name = self.name, mid = values[0], vis = values[1])
        self.debit(values[2])

    def insert_rent(self, values):
        self.curs.execute('''
            insert into Rent values(:name, :mid, sysdate, 'S', :vis)''',
            name = self.name, mid = values[0], vis = values[1])
        self.debit(values[2])

    def insert_waiting(self, mid):
        try:
            self.curs.execute('''
                insert into WaitingList values(:name, :movieID, sysdate)''',
                name = self.name, movieID = mid)
            print '\n', "You have been placed on the waiting list"
        except IntegrityError:
            print '\n', 'You are already on the waiting list for this movie'

    def debit(self, amount):        
        self.curs.execute('''
            update Customer
            set credit = credit - :fee
            where username = :username''', fee = amount, username = self.name)

    def get_credits(self):
        return self.curs.execute(
            "select credit from Customer where username = '"+self.name+"'").fetchone()[0]

    def get_price(self, mediaID):
        return self.curs.execute('''
            select price
            from Media
            where id = :mid''', mid = mediaID).fetchone()[0]

    def get_fee(self, movieID):
        return self.curs.execute('''
            select s_rentFee
            from Movie
            where mid = :mid''', mid = movieID).fetchone()[0]

    def get_copies(self, movieID):
        return self.curs.execute(
            "select quantity from Movie where mid = "+str(movieID)).fetchone()[0]