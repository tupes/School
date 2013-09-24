import subprocess as sub

# The user's row and column choices must be in this list.
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8']
# For converting strings to bytes that can be sent through the pipe.
encoding = 'UTF-8'
# Each square has roughly these dimensions. Units are determined by Sketchpad.
col_width = 78
row_height = 55

# Stores a dictionary of Square objects, initialized to None color.
# Each key is a concatenated string in row+col format.
class Board(object):
    def __init__(self):
        self.exists = False
        self.image = Image()
    
    # Draw the lines and starting pieces on the board.
    def create(self):
        if self.exists:
            self.image.clear()
        self.image.draw_new_board()
        self.squares = {}
        self.create_squares()
        self.initial_position()
        self.exists = True
    
    def delete(self):
        self.image.delete()
    
    # Create the starting pieces.
    def initial_position(self):
        self.change_square(self.squares['33'], 'w')
        self.change_square(self.squares['34'], 'b')
        self.change_square(self.squares['43'], 'b')
        self.change_square(self.squares['44'], 'w')
    
    # Create and store Square objects
    def create_squares(self):
        for row in range(8):
            for col in range(8):
                key = str(row) + str(col)
                self.squares[key] = Square(row, col)
    
    # Change each Square in a list of square objects.
    def change_squares(self, squares):
        key = squares[0].row + squares[0].col
        color = switch(self.squares[key].color)
        for square in squares[:-1]:
            key = square.row + square.col
            self.change_square(self.squares[key])
        key = squares[-1].row + squares[-1].col
        self.change_square(self.squares[key], color)
    
    # If a color is given, the square doesn't contain a piece and can be drawn
    # immediately. Otherwise, erase the piece before drawing the new one.
    def change_square(self, square, color=None):
        if color:
            self.image.change_piece('draw', square, color)
        else:
            piece = square.color
            self.image.change_piece('erase', square, piece)
            color = switch(piece)
            self.image.change_piece('draw', square, color)
        square.color = color

# Opens a pipe to drawing executable Sketchpad.jar, and sends it the
# coordinates of lines to be drawn and erased.
class Image(object):
    def __init__(self):
        self.pipe = sub.Popen('./Sketchpad.jar', stdin=sub.PIPE).stdin
        self.max_y = '640'
        self.max_x = '450'
    
    # Closes Sketchpad.
    def delete(self):
        self.pipe.write(bytes('end\n', encoding))
        self.pipe.flush()
    
    # Clears the screen if the user starts a new game.
    def clear(self):
        self.pipe.write(bytes('clearScreen\n', encoding))
        self.pipe.flush()
    
    # Draws the grid lines, creating the 64 visual squares.
    def draw_new_board(self):
        col = 0
        for vertical_line in range(7):
            col += col_width
            y = str(col)
            self.change_line('draw', y, '0', y, self.max_x)
        
        row = 0
        for horizontal_line in range(7):
            row += row_height
            x = str(row)
            self.change_line('draw', '0', x, self.max_y, x)
    
    # Simply determines whether the change will be to black or white.
    def change_piece(self, change, square, color):
        if color == 'b':
            self.change_black(change, square)
        else:
            self.change_white(change, square)
    
    # Draw or erase solid square, representing black
    def change_black(self, change, square):
        for col in range(square.first_y, square.last_y):
            x1 = str(square.first_x)
            x2 = str(square.last_x)
            self.change_line(change, str(col), x1, str(col), x2)
    
    # Draw or erase X, representing white.
    def change_white(self, change, square):
        x1 = str(square.first_x)
        x2 = str(square.last_x)
        y1 = str(square.first_y)
        y2 = str(square.last_y)
        self.change_line(change, y1, x1, y2, x2)
        self.change_line(change, y1, x2, y2, x1)
    
    # Draw or erase a single line by passing command and 
    # coordinates to Sketchpad.
    def change_line(self, change, y1, x1, y2, x2):
        y1 = ' ' + y1
        x1 = ' ' + x1
        y2 = ' ' + y2
        x2 = ' ' + x2
        self.pipe.write(bytes(change+"Segment"+y1+x1+y2+x2+'\n', encoding))
        self.pipe.flush()

# Stores the color and drawing coordinates for each square.
class Square(object):
    def __init__(self, row, col):
        self.color = None
        row += 1
        col += 1
        self.middle_y = int((col * col_width) - (col_width * 0.5))
        self.middle_x = int((row * row_height) - (row_height * 0.5))
        self.first_y = self.middle_y - 20
        self.last_y = self.middle_y + 20
        self.first_x = self.middle_x - 20
        self.last_x = self.middle_x + 20

# INPUT FUNCTIONS

# Loop until the user enters 'quit' or a valid response.
def get_user_input(color):
    print('Player ' + format(color) + "'s turn")
    while 1:
        row = input('Row: ')
        if row == 'quit':
            quit_message()
            return 'quit'
        elif row == 'help':
            help_message()
            continue
        col = input('Column: ')
        if col == 'quit':
            quit_message
            return 'quit'
        elif col == 'help':
            help_message()
            continue
        action = is_valid_response(row, col)
        if not action:
            error_message('response')
        else:
            # The user enters the rows and cols as 1-8, but these are
            # internally stored as 0-7.
            return (int(row) - 1, int(col) - 1)

def get_play_again():
    answer = input('Play again? ("y" for yes): ')
    if answer == 'y': return True
    else: return False


# OUTPUT FUNCTIONS

def welcome_message():
    print('\nWelcome to the game of Reversi!') 
    print('To see the rules of the game, enter "help" when ' +
            'allowed to play.')
    print('To quit the game, enter "quit".')
    print('Please ensure that the file "Sketchpad.jar" is in your ' +
              'current directory.')
    print('Each Row and Column must be between 1 and 8.')
    print('Rows get bigger from left to right, and Columns get bigger ' +
            'from top to bottom.')    

def new_game_message():
    print('Starting a new game.')

def help_message():
    print('The object of the game is to have as many of your pieces on ' +
              'the board as possible when the game ends. The game ends when' +
              ' neither player can play anymore. A legal play is when you ' +
              'place one of your pieces on a square adjacent to one of ' +
              "your opponent's pieces (left/right, above/below, or " +
              "diagonal), and this creates at least one straight occupied " +
              "line between the new piece and one of your other pieces, " +
              "with at least one of your opponent's pieces in between them.")              

# culprit can be either 'response' or 'move'.
def error_message(culprit):
    print('Sorry, that was an invalid ' + culprit + '. Please try again.')

def show_score(color, pieces):
    score = str(pieces)
    print('Player', format(color) + "'s", 'score:', score)

def show_winner(color):
    winner = format(color)
    if winner:
        print('Player', winner, 'wins!')
    # If color is None, format returns None.
    else:
        print('Game is a draw!')

def quit_message():
    print('Quitting current game.')

def exit_message():
    print('Thanks for playing!')


# UTILITY FUNCTIONS
def format(color):
    if color == 'b': return 'Black'
    elif color == 'w': return 'White'

def switch(color):
    if color == 'b': return 'w'
    elif color == 'w': return 'b'

def is_valid_response(row, col):
    if row not in NUMBERS or col not in NUMBERS: return False
    return True
