"""
author: Csaba Szepesvari, Kevin Quinn, Jorg Sander
Python Module that implements the Minesweeper game logic.  This means the
uncovering, initialization, mine placement, etc.
"""

from minesweeperUI_TK import *

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
	#game.switch_bindings('menu')
	displayMenu()

def onNewGame():
	"""Starts a new game.  Clears the board, resets variables and events, and starts the timer"""
	game.new_game()
	game.display()
	displayNewGame()
	ontimer(100, onTime)
	stopwatchStart()

def onTime():
	"""Updates the time on the GUI"""
	displayElapsedTime(stopwatchGetElapsed())
	ontimer(100, onTime)

def onQuitGame():
	"""Displays a message and exits the main loop"""
	displayBye()
	exitMainLoop()

def onRestartGame():
	"""Restarts the game, by creating a new mine field and displaying it"""
	onNewGame()

def onUncoverCellStart(x, y):
	"""The g_EVENT_CLICK event"""
	if game.get_status(x, y) == g_HIDDEN:
		displayUncoverCellStart(x, y)

def onUncoverCell(x,y):
	"""Checks the current square, determines the status of the board, and
	the status of the game.  If valid and not a mine the square is uncovered"""
	status = game.check_status(x, y)
	if status != 'valid':
		if status == 'invalid': displayInvalidXY(x, y)
		elif status == 'flagged': displayCannotOpenFlagged()
		displayOptions()
	else:
		game.uncover_cell(x, y)


def onFlagCell(x,y):
	"""Toggles the square to be flagged.  If already flagged then remove its status"""
	status = game.check_status(x, y)
	if status == 'invalid': 
		displayInvalidXY(x, y)
		displayOptions()
	else:
		if status == 'valid' or status == 'flagged':
			game.toggle_flag(x, y)
		game.display()


class Minesweeper:
	
	def __init__(self):
		self.max_flags = 10
		events = [g_EVENT_NEWGAME, g_EVENT_QUIT,
			g_EVENT_UNCOVER, g_EVENT_UNCOVER_START, g_EVENT_FLAG, g_EVENT_RESTART, g_EVENT_MENU]
		funcs = [onNewGame, onQuitGame, onUncoverCell, onUncoverCellStart, onFlagCell, onRestartGame, onMainMenu]
		twoargs = [False, False, True, True, True, False, False]
		for f in range(len(funcs)):
			onevent(events[f], funcs[f], twoargs[f])
	
#============================================#
# Functions for the minesweeper game logic #
#============================================#

	def new_game(self):   
		"""initializes a new game by refreshing the status variables and minefield"""
		self.board = randomMinefield()
		self.initializeMineCounts()
		self.hidden_cells = g_rows * g_cols
		self.outcome = g_UNDET # Possible values: g_UNDET, g_WON, g_LOST
		self.used_flags = 0

	def initializeMineCounts(self):
		"""calculates the mine counts for each cell not containing a mine""" 
		for row in range(g_rows):
			for col in range(g_cols):
				if self.get_value(row, col) != g_MINE:
					self.set_value(row, col, self.mine_count(row, col))
	
	def mine_count(self, row, col):
		mines = 0
		for r in range(-1, 2):
			for c in range(-1, 2):
				try:
					if self.get_value(row + r, col + c) == g_MINE: mines += 1
				except KeyError: continue
		return mines
	
	def get_value(self, row, col):
		return self.board[row, col][g_cell_value]
		
	def get_status(self, row, col):
		return self.board[row, col][g_cell_status]
	
	def set_value(self, row, col, value):
		self.board[row, col][g_cell_value] = value
		
	def set_status(self, row, col, status):
		self.board[row, col][g_cell_status] = status

	def check_status(self, row, col):
		if not valid_coords(row, col): return 'invalid'
		elif self.get_status(row, col) == g_OPEN: return 'open'
		elif isFlagged(self.get_status(row, col)): return 'flagged'
		return 'valid'

	def uncover_cell(self, row, col): 
		"""opens the user-specified cell (row, col) if it is hidden, calls 
		recursiveUncover(row, col), checks and handles if the game is won or lost"""
		value = self.get_value(row, col)
		if value == g_MINE:
			self.set_status(row, col, g_EXPLODED)
			self.outcome = g_LOST
		else:
			self.recursiveUncover(row, col)
			displayUncoverCellEnd(row, col)
		self.display()
	
	def recursiveUncover(self, row, col):
		"""opens up" a user-specified cell (row, col) that is assumed to be hidden! 
		   If the opened cell has no mines in its neighbourhood, it 
		   opens up hidden neighbours of cell (row, col) recursively"""
		self.set_status(row, col, g_OPEN)
		self.hidden_cells -= 1
		if self.hidden_cells <= g_mines:
			self.outcome = g_WON
		if self.get_value(row, col) == 0:
			for r in range(-1, 2):
				for c in range(-1, 2):
					if r == 0 and c == 0: continue
					try:
						if self.get_value(row + r, col + c) != g_MINE and \
							self.get_status(row + r, col + c) == g_HIDDEN:
							self.recursiveUncover(row + r, col + c)
					except KeyError: continue
	
	def toggle_flag(self, row, col):
		"""sets a flag for cell (row, col) if there is none; removes the flag if one
		   is already set"""
		if isFlagged(self.get_status(row, col)):
			self.set_status(row, col, g_HIDDEN)
			self.used_flags -= 1
		else:
			if self.used_flags >= self.max_flags: return
			self.set_status(row, col, g_FLAGGED)
			self.used_flags += 1
	
	def display(self):
		displayBoard(self.board, self.outcome)
		if self.outcome != g_UNDET:
			stopwatchStop()
			displayGameOver(self.outcome)
		else:
			displayOptions()


def main():
	# start the menu
	UI_initialize()
	onNewGame()
	mainLoop()

game = Minesweeper()
if __name__=="__main__":
	main()
