# playreversi.py
# -- Controller for Reversi game.
#
# Copyright 2011, Rick Valenzano.
# All rights reserved.

import sys
from model import *
from view import print_board, get_user_move, get_player_info, print_help_info, \
     move_inverter, HUMAN_TYPE, RANDOM_TYPE, MINIMAX_TYPE, get_pos_int_from_user
from computerplayers import get_random_move, get_minimax_move
import time
import random

# gets a move by a computer agent. Calls the desired move generator
def get_computer_move(player_type, params):
    
    if player_type == RANDOM_TYPE:
        return get_random_move(board)
    elif player_type == MINIMAX_TYPE:
        print("Minimax move being computed")
        return get_minimax_move(board, params[0])
    
# The main board
board = ReversiLogic()

# The players and the params for each
black_type = HUMAN_TYPE
black_params = []
white_type = HUMAN_TYPE
white_params = []

# whether to print of not
need_to_print = True

while True:
    
    # Only print if a valid move was entered
    if need_to_print:
        print()
        print_board(board)
        print()
        need_to_print = False
    
    # exit if the game is over
    if board.whose_turn() == NONE:
        print("GAME OVER")
        if board.get_winner() == BLACK:
            print("BLACK WINS")
        elif board.get_winner() == WHITE:
            print("WHITE WINS")
        else:
            print("TIE GAME")
        break

    move = None
    
    # calls appropriate computer player if need to
    if board.whose_turn() == BLACK and black_type != HUMAN_TYPE:
        start = time.time()
        move = get_computer_move(black_type, black_params)
        print("It took", time.time()-start, "seconds to get the move")
        print("The computer selected move", move_inverter(move))
    elif board.whose_turn() == WHITE and white_type != HUMAN_TYPE:
        start = time.time()
        move = get_computer_move(white_type, white_params)
        print("It took", time.time()-start, "seconds to get the move")
        print("The computer selected move", move_inverter(move))
    else: # user is entering info
        user_input = input("Enter move or command (or 'help'): ").strip()
    
        if user_input == "help":
            print_help_info()
            need_to_print = True
        elif user_input == "seed":
            seed = get_pos_int_from_user("random num generator seed")
            random.seed(seed)
        elif user_input == "blackplayer":
            (black_type, black_params) = get_player_info("black")
        elif user_input == "whiteplayer":
            (white_type, white_params) = get_player_info("white")
        else:
            move = get_user_move(user_input)
    
    
    if move != None:
        if board.is_legal_move(move[0], move[1]):
            board.make_move(move[0], move[1])
            need_to_print = True
        else:
            print("Not a legal move")
    
