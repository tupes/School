

class ReversiLogic(object):
    def __init__(self):
        self.turn = 'b'
        self.board = Board()
    
    # Check if the current self.turn can play. If not, change to the other
    # player. If he can't play either, return None (game over).
    def get_whose_turn(self):
        if self.can_play():
            return self.turn
        else:
            self.turn = switch(self.turn)
            if self.can_play():
                return self.turn
        return None
    
    # Iterate through every square on the board until a legal move is
    # found. If none is found, the current self.turn can't play.
    def can_play(self):
        for row in range(8):
            for col in range(8):
                if self.legal_attacks(row, col):
                    return True
        return False
    
    # Get a list of all of the attack lines created by playing this square.
    # If it's empty, the move is invalid. Otherwise, change the square and
    # flip the pieces on the attack lines. Return changed squares as a list of
    # Square objects to be graphically changed.
    def make_move(self, row, col):
        directions = self.legal_attacks(row, col)
        if not directions: return False
        self.board.squares[get_key(row, col)] = self.turn
        self.turn = switch(self.turn)
        return self.board.flip(row, col, directions)
    
    # If there's already a piece on this square, it can't be a legal move.
    # Otherwise, return a (possibly empty) list of all of the attack lines.
    def legal_attacks(self, row, col):
        if self.board.squares[get_key(row, col)]: return False
        return self.board.attacks(row, col, self.turn)
    
    # Return the number of the given player's pieces on the board.
    def count_pieces(self, color):
        pieces = 0
        for row in range(8):
            for col in range(8):
                if self.board.squares[get_key(row, col)] == color:
                    pieces += 1
        return pieces

# Stores a dictionary of each square's color, initialized to None.
# Each key is a concatenated string in row+col format. See get_key().
class Board(object):
    def __init__(self):
        self.squares = {}
        for row in range(8):
            for col in range(8):
                key = get_key(row, col)
                self.squares[key] = None
        # Create the starting pieces.
        self.squares['33'] = 'w'
        self.squares['34'] = 'b'
        self.squares['43'] = 'b'
        self.squares['44'] = 'w'
        steps = [-1, 0, 1]
        steps = [(r_step, c_step) for r_step in steps for c_step in steps]
        steps.remove((0, 0))
        # Steps is a list of tuples, representing all possible directions from
        # a given square. Tuple is in (row_step, col_step) format.
        self.steps = steps
    
    def attacks(self, row, col, color):
        attack_lines = []
        opponent = switch(color)
        # Check in every adjacent square for the opponent's color.
        for direction in self.steps:
            row_step = direction[0]
            col_step = direction[1]
            # Use a try statement because some adjacent squares will be
            # off the board, resulting in a key error.
            try:
                key = get_key(row + row_step, col + col_step)
                # If adjacent square contains the opponent, continue in that
                # direction to determine if it meets up with a player's piece.
                if self.squares[key] == opponent:
                    row_index = row
                    col_index = col
                    while 1:
                        row_index += row_step
                        col_index += col_step
                        key = get_key(row_index, col_index)
                        # Check to see if there's a piece on this square.
                        if self.squares[key]:
                            # Now check if the piece is one of the players.
                            if self.squares[key] != opponent:
                                # We have found an attack line.
                                attack_lines.append(direction)
                                # Break from this direction to try others.
                                break
                        # Found an empty square. Move on to the next direction
                        else: break
            # If we check a square not on the board, just move on to the next.
            except KeyError: continue
        return attack_lines
    
    def flip(self, row, col, directions):
        # target is the color we'll be changing to.
        target = self.squares[get_key(row, col)]
        # squares is the list of squares that need to be graphically updated.
        squares = []
        # Each direction is an attack line.
        for direction in directions:
            row_index = row
            col_index = col
            # Continue flipping pieces in this direction until target is found
            while 1:
                row_index += direction[0]
                col_index += direction[1]
                key = get_key(row_index, col_index)
                if self.squares[key] == target: break
                # Flip piece.
                self.squares[key] = target
                # Add this square to list that must be graphically updated.
                squares.append(Square(row_index, col_index))
        # The played square must be graphically updated too.
        squares.append(Square(row, col))
        return squares

# Simple data storage object to return to the main function.
# Each square returned must be updated.
class Square(object):
    def __init__(self, row, col):
        self.row = str(row)
        self.col = str(col)

# UTILITY FUNCTIONS
def get_key(row, col):
    return str(row) + str(col)

def switch(color):
    if color == 'b': return 'w'
    elif color == 'w': return 'b'
