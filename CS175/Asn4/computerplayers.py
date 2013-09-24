# computerplayers.py
# -- Computer players for Reversi
#
# Copyright 2011, Rick Valenzano.
# 
# Modified by Mark Tupala for CMPUT 175 F11 Assignment 4

from model import *
from view import move_inverter
import copy
import random
import operator

BLACK_WIN = 1000000
BLACK_LOSS = -1000000

##########################
# Random Computer Player
##########################
def get_random_move(board):
    """Returns a random move that is applicable in the current state. 
    Assumes there is at least one move applicable in the current state."""

    player = board.whose_turn()
    board.compute_legal_moves(player)
    num_moves = len(board.legal_moves)
    move_num = random.randint(0, num_moves - 1)
    random_move = board.legal_moves[move_num]

    return random_move
#########################
# End of Random Player
#########################

#########################
# Evaluation Function
#########################
def count_corners(board, player):
    """Counts the number of corners belonging to the specified player. """
    count = 0
    if board.occupied_by(0, 0) == player:
        count+=1
    elif board.occupied_by(0, BOARD_SIZE - 1) == player:
        count += 1
    elif board.occupied_by(BOARD_SIZE - 1, 0) == player:
        count += 1
    elif board.occupied_by(BOARD_SIZE - 1, BOARD_SIZE - 1) == player:
        count += 1
    return count
    
def chip_count_eval_function(board):
    """Counts the difference in the number of chips that each player has. """
    return board.num_chips(BLACK) - board.num_chips(WHITE)

def combo_eval_function(board):
    """A combination of the chip count evaluation function and the 
    corner counting evaluation function.
    """
    value = 0
    value += 10*count_corners(board, BLACK)
    value -= 10*count_corners(board, WHITE)
    value += chip_count_eval_function(board)
    
    return value
#########################
# End of Evaluation Function
#########################

#########################
# Minimax Algorithm
#########################
def utility(board):
    winner = board.get_winner()
    if winner == BLACK: return BLACK_WIN
    elif winner == WHITE: return BLACK_LOSS
    else: return 0    

def get_minimax_value(board, depth):
    """Gets the current minimax value for the `board` at a given `depth`."""
    
    # if the depth limit is reached, return the evaluated value of the board
    if depth <= 0: 
        return combo_eval_function(board)
    
    # if the game would be over, return the outcome
    player = board.whose_turn()
    if player == NONE: 
        return utility(board)
    
    # Initialize the comparison function and worst possible value
    if player == BLACK:
        chooseBest = max
        best_val = BLACK_LOSS
    else:
        chooseBest = min
        best_val = BLACK_WIN
    
    board.compute_legal_moves(player)
    # get the minimax value for each possible move
    for row, col in board.legal_moves:
        new_board = copy.deepcopy(board)
        new_board.make_move(row, col)
        # check to see if this move is better than the current best
        best_val = chooseBest(best_val, get_minimax_value(new_board, depth-1))
    return best_val
    
def get_minimax_move(board, depth):
    """Get a moved based on the minimax value."""
    
    # get the current player and its possible moves
    player = board.whose_turn()
    board.compute_legal_moves(player)
    if len(board.legal_moves) == 1:
        return board.legal_moves[0]
    
    # Initialize comparison function and worst possible value
    if player == BLACK:
        isBetter = operator.gt
        minimax_value = BLACK_LOSS
    else:
        isBetter = operator.lt
        minimax_value = BLACK_WIN
    best_move_index = 0
    
    print("Minimax Values:")
    # get the minimax value for each possible move
    for move_index in range(len(board.legal_moves)):
        new_board = copy.deepcopy(board)
        row, col = board.legal_moves[move_index]
        new_board.make_move(row, col)
        move_value = get_minimax_value(new_board, depth - 1)
        current_move = board.legal_moves[move_index]
        print("\t", move_inverter(current_move), ":", move_value)
        
        # check to see if this move is better than the current best
        if isBetter(move_value, minimax_value):
            minimax_value = move_value
            best_move_index = move_index
    
    best_move = board.legal_moves[best_move_index]
    return best_move
#########################
# End of Minimax Algorithm
#########################
