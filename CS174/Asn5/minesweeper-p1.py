"""
author: Csaba Szepesvari, Kevin Quinn, Jorg Sander
Python Module that implements the Minesweeper game logic.  This means the
uncovering, initialization, mine placement, etc.
"""

from minesweeperUI_Text import *

#============================================#
# Representation of the game status          #
#============================================#

# Dictionary, representing the minefield.
# The keys are tuples of row and column coordinates of cells.
# Each "cell" is associated with a list of 2 elements.
#
# In particular,
# 
# g_mine_field[row,col][g_cell_value]==g_MINE 
#
# if there is a mine at (row,col), otherwise
# 
# g_mine_field[row,col][g_cell_value]=g_EMPTY.
#
# Further,
#
# g_mine_field[row,col][g_cell_status] gives the 'status' of the 
# player knows. Possible values are:
# g_HIDDEN
#   (for cells that have not been uncovered and which are not flagged),
# g_OPEN
#   (for cells that have been uncovered),
# g_FLAGGED
#   (for cells that have been marked as a mine),
# g_EXPLODED
#   (for a cell with a mine that has been uncovered)


def valid_coords(row, col):
	return 0 <= row < g_rows and 0 <= col < g_cols

#============================================#
# Event handling functionality               #
#============================================#
def onMainMenu():
	"""Displays the menu and registers the related events"""
	game.switch_bindings('menu')
	displayMenu()

def onNewGame():
	"""Starts a new game.  Clears the board, resets variables and events"""
	game.new_game()    
	game.switch_bindings('game')
	game.display()

def onQuitGame():
	"""Displays a message and exits the main loop"""
	displayBye()
	exitMainLoop()

def onRestartGame():
	"""Restarts the game, by creating a new mine field and displaying it"""
	onNewGame()

def onUncoverCell(x,y):
	"""Checks the current square, determines the status of the board, and
	the status of the game.  If valid and not a mine the square is uncovered"""
	if game.check_valid(x, y) and game.not_flagged(x, y): 
		game.uncover_cell(x, y)

def onFlagCell(x,y):
	"""Toggles the square to be flagged.  If already flagged then remove its status"""
	if game.check_valid(x, y): 
		game.toggle_flag(x, y)


class Minesweeper:        
	events = [g_EVENT_NEWGAME, g_EVENT_QUIT,
			  g_EVENT_UNCOVER, g_EVENT_FLAG, g_EVENT_RESTART, g_EVENT_MENU]
	menu_funcs = [onNewGame, onQuitGame, None, None, None, None]
	game_funcs = [None, None, onUncoverCell, onFlagCell, onRestartGame, onMainMenu]
	two_args = [False, False, True, True, False, False]
#============================================#
# Functions for the minesweeper game logic #
#============================================#

	def new_game(self):   
		"""initializes a new game by refreshing the status variables and minefield"""
		self.board = randomMinefield()
		self.hidden_cells = g_rows * g_cols
		self.outcome = g_UNDET # Possible values: g_UNDET, g_WON, g_LOST
	
	def switch_bindings(self, phase):
		if phase == 'menu': 
			funcs = self.menu_funcs
		else:
			funcs = self.game_funcs
		for f in range(len(funcs)):
			onevent(self.events[f], funcs[f], self.two_args[f])
	
	def get_value(self, row, col):
		return self.board[row, col][g_cell_value]
		
	def get_status(self, row, col):
		return self.board[row, col][g_cell_status]
	
	def set_value(self, row, col, value):
		self.board[row, col][g_cell_value] = value
		
	def set_status(self, row, col, status):
		self.board[row, col][g_cell_status] = status
	
	def check_valid(self, row, col):
		if not valid_coords(row, col): 
			displayInvalidXY(row, col)
			displayOptions()
		elif self.get_status(row, col) == g_OPEN: pass
		else: return True
		return False
		
	def not_flagged(self, row, col):
		if isFlagged(self.get_status(row, col)): 
			displayCannotOpenFlagged()
			self.display()
			return False
		return True
	
	def uncover_cell(self, row, col): 
		"""opens the user-specified cell (row, col) if it is hidden checks and handles
		 if the game is won or lost"""
		value = self.get_value(row, col)
		if value == g_MINE:
			self.set_status(row, col, g_EXPLODED)
			self.outcome = g_LOST
		else:
			self.set_status(row, col, g_OPEN)
			self.hidden_cells -= 1
			if self.hidden_cells <= g_mines:
				self.outcome = g_WON
		self.display()
		
	
	def toggle_flag(self, row, col):
		"""sets a flag for cell (row, col) if there is none; removes the flag if one
		   is already set"""
		if isFlagged(self.get_status(row, col)):
			self.set_status(row, col, g_HIDDEN)
		else:
			self.set_status(row, col, g_FLAGGED)
		self.display()
	
	def display(self):
		displayBoard(self.board, self.outcome)
		if self.outcome != g_UNDET:
			displayGameOver(self.outcome)
			onMainMenu()
		else:
			displayOptions()

def main():
	# start the menu
	UI_initialize()
	onMainMenu()
	mainLoop()

game = Minesweeper()
if __name__=="__main__":
	main()
