from sys import argv
from InfoMode import *
from FriendsMode import *
from MediaMode import *
from MoviesMode import *

def main():
    conn = get_connection()
    cursor = conn.cursor()
    username = login(cursor)
    serve(cursor, username)
    conn.commit()
    conn.close()

def get_connection():
    #try:
        name = raw_input("Please enter the Oracle username: ")
        password = raw_input("Please enter the Oracle password: ")
        if len(argv) > 1:
            url = raw_input("Please enter the URL of the database server: ")
        else:
            url = 'gwynne.cs.ualberta.ca:1521'
        connection_string = name + '/' + password + '@' + url 
        return connect(connection_string)
    #except:
        print 'Unable to connect to database server'
        exit()

def login(curs):
    while 1:
        username = raw_input('Please enter your username: ')
        if len(username) > USERNAME_SIZE:
            print 'Invalid username'
        username = username.ljust(USERNAME_SIZE)
        if check_username(curs, username):
            return username
        else:
            print 'Invalid username'

def check_username(curs, username):
    curs.execute('select username from Customer where username = :name', 
                 name = username).fetchone()
    if curs.rowcount:
        return True        
    return False

def serve(curs, username):
    while 1:
        print '\n', 'Main Menu'
        command = raw_input("Please enter a command ('"+help_command+"' to see options): ")
        if command == info:
            InfoMode(curs, username)
        elif command == friends:
            friends_mode(curs, username)
        elif command == media:
            MediaMode(curs, username)
        elif command == movies:
            MoviesMode(curs, username)
        elif command == help_command:
            display_options()
        elif command == exit_command:
            break
        else:
            print '\n', 'Unknown command. Please try again'

def display_options():
    print "Enter 'info' to view and edit your personal information"
    print "Enter 'friends' to view and edit your friends list"
    print "Enter 'media' to view and purchase available items"
    print "Enter 'movies' to view and rate your movies"
    print "Enter 'q' to exit"

if __name__ == '__main__':
    main()