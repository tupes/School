
from Mode import *

class RemoveFriend(Mode):    
    def __init__(self, curs, name):
        self.query = (
            "select username "
            "from friend "
            "join customer on ("
              "username != '"+name+"' and "
              "user1 in ('"+name+"', username) and " 
              "user2 in ('"+name+"', username))")
        
        self.prompt = "Enter 'remove' followed by the user's name, or anything else to return to the main menu: "
        self.commands = {'remove': self.remove}
        Mode.start(self, curs, name)

    def output(self, record):
        value = record[0].strip()
        self.cache.add(value)
        return value

    def remove(self, value):
        self.process(value[0], self.validate, self.delete)

    def validate(self, value):
        if value not in self.cache:
            print '\n', "Sorry, you are not friends with that user"
            return False
        return value

    def delete(self, name):
        self.curs.execute('''
            delete from friend
            where
                (user1 = :username and user2 = :other_name) or
                (user1 = :other_name and user2 = :username)''',
            username = self.name, other_name = name.ljust(USERNAME_SIZE))

    def success(self, name):
        print '\n', 'Deleted ' + name + ' from friends'

class AddFriend(Mode):
    def __init__(self, curs, name):
        self.prompt = "Enter 'add' followed by the user's name, or anything else to return to the main menu: "
        self.double_message = "You're already friends with that user"        
        self.commands = {'add': self.add}
        Mode.start(self, curs, name)
    
    def get(self):
        return self.curs.execute('''
            select distinct c1.username
            from customer c2
            join customer c1 on (c1.username != :name)
            join customer c3 on (c3.username = :name)
            join friend f1 on (f1.user1 in (c1.username, c2.username) and f1.user2 in (c1.username, c2.username))
            join friend f2 on (f2.user1 in (c2.username, :name) and f2.user2 in (c2.username, :name))
            where
              not exists(
                select c3.username
                from friend f3
                where
                  c1.username in(f3.user1, f3.user2) and
                  c3.username in(f3.user1, f3.user2))''', 
            name = self.name).fetchall()

    def output(self, record):
        value = record[0].strip()
        self.cache.add(value)
        return value

    def add(self, value):
        self.process(value[0], self.validate, self.insert)

    def validate(self, value):
        if value not in self.cache:
            print '\n', "Sorry, user must be from suggestion list"
            return False
        return value

    def insert(self, name):
        self.curs.execute("insert into friend values(:me, :other)",
                          me = self.name, other = name.ljust(USERNAME_SIZE))

    def success(self, name):
        print '\n', "Added " + name + " to friends"


def friends_mode(curs, name):
    command = raw_input("\nEnter 'friends' to see your friends, 'suggest' to see friend suggestions, or anything else to return to the main menu: ")
    if command == 'friends':
        RemoveFriend(curs, name)
    elif command == 'suggest':
        AddFriend(curs, name)