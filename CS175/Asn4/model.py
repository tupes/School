# model.py
# -- Model component of Reversi game.
#
# Copyright 2011, Rick Valenzano.
# All rights reserved.

#some constants
WHITE = 2
BLACK = 1
NONE = 0
TIE = -1

# This is only so that I could more easily test winning conditions 
# by doing so on smaller boards
BOARD_SIZE = 8

# A class for Reversi logic. It contains a data structure for the board as 
# a list of lists
class ReversiLogic:
    
    # Constructor, builds a board given by the size above, initializes the 
    # board position, chip counts, whose turn it is, and generates original
    # list of legal moves
    def __init__(self):
    
        self._board = []
        self._adjacent = []
        for row in range(BOARD_SIZE):
            self._board.append([NONE]*BOARD_SIZE)
            self._adjacent.append([False]*BOARD_SIZE)
            
        # initial moves
        self._board[BOARD_SIZE//2 - 1][BOARD_SIZE//2 - 1] = WHITE
        self._board[BOARD_SIZE//2][BOARD_SIZE//2] = WHITE
        self._board[BOARD_SIZE//2 - 1][BOARD_SIZE//2] = BLACK
        self._board[BOARD_SIZE//2][BOARD_SIZE//2 - 1] = BLACK

        # initial turn
        self._turn = BLACK
        
        self._chip_count = {WHITE : 2, BLACK: 2}
        
        self.legal_moves = []
        
        self._initialize_adjacency_list()
        self.compute_legal_moves(self._turn)
        
    
    # Updates the adjacency list after placing a piece at the current location
    def _update_adjacency_list(self, row, col):
        for x in (-1,1,0):
            for y in (-1,1,0):
                # skips [0, 0]
                if x == 0 and y == 0:
                    continue
                if (row + x < BOARD_SIZE and row + x >= 0 and 
                    col + y < BOARD_SIZE and col + y >= 0 and
                    self._board[row + x][col + y] == NONE):
                    self._adjacent[row + x][col + y] = True

    # Updates the adjacency list at the beginning
    def _initialize_adjacency_list(self):
        # scan every square to update all 
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self._board[row][col] != NONE:
                    self._update_adjacency_list(row, col)
		    
    # Returns whose turn it is
    def whose_turn(self):
        return self._turn
    
    # Return the number of chips each player has on the board in the current
    # state
    # player - the person whose chips are wanted
    def num_chips(self, player):
        if player != WHITE and player != BLACK:
            raise RuntimeError("Player", player, "is undefined")
        
        # return appropriate chip count
        if player == WHITE:
            return self._chip_count[WHITE]
        else:
            return self._chip_count[BLACK]
    
    # Returns the number of open squares
    def num_open_squares(self):
        return BOARD_SIZE*BOARD_SIZE - self.white_count - self.black_count
    
    # Returns the winner if the game is finished (TIE if it is tied), and
    # 0 otherwise
    def get_winner(self):

        # if not the end of game
        if self._turn != NONE:
            return NONE
        
        if self._chip_count[WHITE] > self._chip_count[BLACK]:
            return WHITE
        elif self._chip_count[WHITE] < self._chip_count[BLACK]:
            return BLACK
        
        return TIE
    
    # Returns True if the given space is occupied or not
    # row - the row of the position to check
    # col - the column of the position to check
    def occupied_by(self, row, col):
        if row >= BOARD_SIZE or row < 0 or col >= BOARD_SIZE or col < 0:
            raise RuntimeError("Move", row, col, "is undefined")
        
        return self._board[row][col]
    
    # Checks if the give move is legal in the current state
    # row - the row of the position to check
    # col - the column of the position to check
    def is_legal_move(self, row, col):
        for pos in self.legal_moves:
            if pos[0] == row and pos[1] == col:
                return True
        
        return False
    
    # Checks if the given move is legal due to the given direction
    # player_to_check - the player whose potential turn we are checking
    # row - the starting row to check
    # col - the starting columng to check
    # row_inc - the delta x value (helps define the direction to check)
    # col_inc - the delta y value (helps define the direction to check)
    def check_direction(self, player_to_check, row, col, row_inc, col_inc):
        
        # if we encounter chips for the other player
        chips_between = False
        check_row = row + row_inc
        check_col = col + col_inc
        other_player = self.other_player(player_to_check)
        
        # makes sure the position to start at is either open or contains the 
        # other player
        assert self.occupied_by(row, col) != other_player, \
               "Invalid call to check_direction: " + str(row) + ", " + str(col)
        
        # iterates in the given direction until we run off the board or we 
        # discover this direction will not invalidate or validate the given
        # move
        while (check_row >= 0 and check_row < BOARD_SIZE and 
               check_col >= 0 and check_col < BOARD_SIZE):
            
            # ran into an empty board
            if self._board[check_row][check_col] == NONE:
                return False
            # have now seen one chip by the other player
            elif self._board[check_row][check_col] == other_player:
                chips_between = True
            # If stumble into one of the current player's chips again
            elif self._board[check_row][check_col] == player_to_check:
		# if there is a chip between start position and current position
                # then this direction makes the move valid
                if chips_between:
                    return True
                # if have two of current player's chips in a row
                else:
                    return False
            
            check_row += row_inc
            check_col += col_inc
        
        return False
    
    # Checks if the given move is a legal move
    # turn_to_check - the player whose turn we are checking
    # row - the row of the position to check
    # col - the column of the position to check
    def check_move(self, player_to_check, row, col):
        
        # must be an empty position
        if self._board[row][col] != NONE:
            return False

        # check a single tile in each direction
        # for [row, col], [1, 0] is North, [1, 1] is Northeast, [0, 1] is East,
        # [-1, 1] is Southeast, [-1, 0] is South, [-1, -1] is Southwest,
        # [-1, 0] is West, [-1, 1] is Northwest
        # [0, 0] will be skipped
        for x in (-1,1,0):
            for y in (-1,1,0):
                # skips [0, 0]
                if x == 0 and y == 0:
                    continue

                if self.check_direction(player_to_check, row, col, x, y):
                    return True
        
        return False
    
    # Returns a list of all the legal moves
    # turn_to_check - the player whose legal moves we want
    def compute_legal_moves(self, player_to_check):
        assert self._turn == WHITE or self._turn == BLACK, "Incorrect Turn"
    
        self.legal_moves = []
        
	    # scan every square to see if it's a legal move
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if (self._adjacent[row][col] == True and
                    self.check_move(player_to_check, row, col)):
                    self.legal_moves.append([row, col])
        
    # Returns the opposite player of the entered move
    # player - the player to reverse
    def other_player(self, player):
        if player == WHITE:
            return BLACK
        return WHITE
    
    # Updates the board with the given move (assume already updated) in the
    # given direction (in terms of the increments). 
    # Assumes it is a legal move
    # update_turn - the player whose turn we are checking
    # row - the row of the position to check
    # col - the column of the position to check
    # row_inc - the delta x value (helps define the direction to check)
    # col_inc - the delta y value (helps define the direction to check)
    def update_board_direction(self, update_player, row, col, row_inc, col_inc):
        assert self.occupied_by(row, col) == update_player, \
               "Incorrect call to update_board_direction: " + str(row) + \
               ", " + str(col)
        
        update_row = row + row_inc
        update_col = col + col_inc
        other_player = self.other_player(update_player)
        
	# start going in the given direction and flipping pieces until you hit one
	# of the pieces of the update player
        while True:
            assert (update_row >= 0 and update_row < BOARD_SIZE and 
                    update_col >= 0 and update_col < BOARD_SIZE), \
                   "Bad stuff here: " + str(update_row) + \
                   ", " + str(update_col)
            
            assert self._board[update_row][update_col] != NONE, \
                   "Bad stuff here: " + str(update_row) + ", " + str(update_col)
            
            if self._board[update_row][update_col] == update_player:
                # make sure it is a good direction
                assert (update_row != row + row_inc or
                        update_col != col + col_inc), \
                       "Bad stuff here: " + str(update_row) + ", " + \
                       str(update_col)
                break
            
            # interchange piece and update chip count
            self._board[update_row][update_col] = update_player
            self._chip_count[update_player] +=1
            self._chip_count[other_player] -= 1
            
            update_row += row_inc
            update_col += col_inc
    
    # Adds the move, updates the board, set of legal moves, chip counts, and
    # whose turn it is
    # row - the row of the position to check
    # col - the column of the position to check
    def make_move(self, row, col):
        if not self.is_legal_move(row, col):
            raise RuntimeError("Move", row, col, "is undefined")
        
        # add the chip to the board
        self._board[row][col] = self._turn
        self._chip_count[self._turn]+= 1
        
        # update adjacency list
        self._adjacent[row][col] = False
        self._update_adjacency_list(row, col)
        
        # update board in each direction
        # for [row, col], [1, 0] is North, [1, 1] is Northeast, [0, 1] is East,
        # [-1, 1] is Southeast, [-1, 0] is South, [-1, -1] is Southwest,
        # [-1, 0] is West, [-1, 1] is Northwest
        # [0, 0] will be skipped
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x == 0 and y == 0:
                    continue
                if self.check_direction(self._turn, row, col, x, y):
                    self.update_board_direction(self._turn, row, col, x, y)
        
        # Try other player for moves
        whose_turn = self.other_player(self._turn)
        
        self.compute_legal_moves(whose_turn)
        
        # other player has no moves
        if len(self.legal_moves) == 0:
            
            # check for more moves by us
            self.compute_legal_moves(self._turn)
            
            # both players have no moves
            if len(self.legal_moves) == 0:
                self._turn = NONE
        else:
            self._turn = whose_turn
