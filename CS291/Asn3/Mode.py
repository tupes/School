
from cx_Oracle import connect, IntegrityError

# global constants
USERNAME_SIZE = TITLE_SIZE = 20
EMAIL_SIZE = 32
exit_command = 'q'
help_command = 'help'
info = 'info'
friends = 'friends'
media = 'media'
movies = 'movies'
vis_options = {'A', 'F', 'N'}

# Abstract base class for the specific modes
class Mode():
    def start(self, curs, name, input_tokens = 2):
        self.curs = curs
        self.name = name
        self.input_tokens = input_tokens
        self.cache = set()
        self.display()
        self.interact()
    
    def display(self):
        records = self.get()
        for record in records:
            print self.output(record)

    def get(self):
        return self.curs.execute(self.query).fetchall()

    def output(self, record):
        mid = str(record[0])
        self.cache.add(mid)
        return self.format(record[1].strip(), mid, str(record[2]))

    def interact(self):
        tokens = raw_input('\n' + self.prompt).split()
        if len(tokens) != self.input_tokens: return
        if tokens[0] not in self.commands: return
        self.commands[tokens[0]](tokens[1:])
        
    def process(self, value, validate_func, sql_func):        
        value = validate_func(value)
        if value: 
            try:
                sql_func(value)
                self.success(value)
            except IntegrityError:
                self.double(value)

    def validate_vis(self, vis):
        if vis in vis_options: return vis
        print '\n', 'Sorry, that is not one of the available options (A, F, N)'
        return False

    def success(self, junk):          
        print '\n', self.success_message

    def double(self, junk):
        print '\n', self.double_message

