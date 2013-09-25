
from Mode import *

class InfoMode(Mode):
    def __init__(self, curs, name):
        self.prompt = ("Enter 'email' or 'vis' followed by the new value to "
            "update, or anything else to return to the main menu: ")
        self.success_message = 'Information updated'
        self.commands = {'email': self.email, 'vis': self.vis} 
        Mode.start(self, curs, name)

    def display(self):
        credit, email, vis = self.get()
        print '\n', 'Username:', self.name.strip()
        print 'Credits:', credit
        print 'Email:', email.strip()
        print 'Email Visibility:', vis
    
    def get(self):
        return self.curs.execute('''
            select credit, email, emailVisibility
            from Customer
            where username = :name''', name = self.name
        ).fetchone()

    def email(self, value):
        self.process(value[0], self.validate_email, self.update_email)

    def vis(self, value):
        self.process(value[0], self.validate_vis, self.update_vis)
    
    def validate_email(self, email):
        if len(email) <= EMAIL_SIZE: return email
        print '\n', 'Sorry, provided email exceeds maximum length'
        return False

    def update_email(self, value):
        self.curs.execute('''
            update customer
            set email = :new_value
            where username = :name''',
            new_value = value, name = self.name)

    def update_vis(self, vis):
        self.curs.execute('''
            update Customer
            set emailVisibility = :new_value
            where username = :name''',
            new_value = vis, name = self.name)
