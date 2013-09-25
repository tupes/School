from sys import argv
from cx_Oracle import connect

exit_command = 'q'
help_command = 'help'

def main():
    conn = get_connection()
    cursor = conn.cursor()
    serve(cursor)
    conn.commit()
    conn.close()

def get_connection():
    try:
        name = raw_input("Please enter the Oracle username: ")
        password = raw_input("Please enter the Oracle password: ")
        if len(argv) > 1:
            url = raw_input("Please enter the URL of the database server: ")
        else:
            url = 'gwynne.cs.ualberta.ca:1521'
        connection_string = name + '/' + password + '@' + url 
        return connect(connection_string)
    except:
        print 'Unable to connect to database server'
        exit()

def serve(curs):
    while 1:
        command = raw_input("Please enter a command('help' to display options): ")
        if command == exit_command:
            break
        elif command == help_command:
            display_options()
        elif command == 'rent check':
            rent_check(curs)
        elif command.startswith('top '):
            get_ratings(curs, command)
        elif command.startswith('more '):
            increase_copies(curs, command)
        else:
            print 'Unknown command. Please try again.'

def display_options():
    print "Enter 'rent check' to update short term rentals to long term"
    print "Enter 'top' followed by the minimum rating and the number of movies"
    print "Enter 'more' followed by the movieID and the number of copies to increase by"

def rent_check(curs):
    records = get_renters(curs)
    for record in records: print record
    curs.execute('''
        update rent
        set rent.rentmode = 'L'
        where 
          rent.rentmode = 'S' and
          sysdate - rent.since > 7''')
    for record in records:
        debit_user(curs, record[0], get_difference(curs, record[1]))
    print '\n', 'Finished updating rent modes'

def debit_user(curs, name, amount):
    curs.execute('''
        update Customer
        set credit = credit - :fee
        where username = :username''', fee = amount, username = name)

def get_ratings(curs, command):
    args = validate(command, float)
    if not args: return
    K, N = args
    records = curs.execute(
        "select movieID, avg(rating) as avg_rating "
        "from Rate "
        "group by movieid "
        "having avg(rating) > " + str(K) + " "
        "order by avg_rating desc").fetchmany(N)
    for record in records:
        print str(record[0]) + ': ' + str(record[1])

def increase_copies(curs, command):
    args = validate(command, int)
    if not args: return
    movieID, copies = args
    print '\n', 'Ordering ' + str(copies) + ' more copies of movie ' + str(movieID)
    curs.execute(
        "update movie "
        "set quantity = " + str(get_copies(curs, movieID) + copies) + " "
        "where mid = " + str(movieID))
    fee = get_fees(curs, movieID)[0]
    names = get_waiting(curs, movieID, copies, fee)
    add_renters(curs, names, movieID, fee)

def validate(command, conv_func):
    tokens = command.split()
    if len(tokens) != 3:
        print 'Invalid format'
        return False
    try:
        return conv_func(tokens[1]), int(tokens[2])
    except ValueError:
        print 'Arguments must be integers'
        return False

def add_renters(curs, names, movieID, fee):
    for name in names:
        curs.execute('''
            insert into Rent values(:username, :mid, sysdate, 'S', 'N')''',
            username = name, mid = movieID)
        debit_user(curs, name, fee)

def get_renters(curs):
    return curs.execute('''
        select username, movieID
        from rent
        where 
          rentmode = 'S' and
          sysdate - since > 7''').fetchall()

def get_difference(curs, movieID):
    short_fee, long_fee = get_fees(curs, movieID)
    return long_fee - short_fee

def get_copies(curs, movieID):
    return curs.execute(
        "select quantity from Movie where mid = "+str(movieID)).fetchone()[0]

def get_waiting(curs, movieID, N, s_fee):
    return [name[0] for name in curs.execute('''
        select c.username
        from customer c
        join waitingList wl on (c.username = wl.username)
        join movie m on (wl.movieID = m.mid and m.mid = :mid)
        where c.credit >= :fee
        order by wl.since''', 
        mid = movieID, fee = s_fee).fetchmany(N)]

def get_fees(curs, movieID):
    return curs.execute("select s_rentFee, l_rentFee from Movie where mid = :mid", mid=movieID
        ).fetchone()

if __name__ == '__main__':
    main()