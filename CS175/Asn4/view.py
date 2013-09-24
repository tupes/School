# view.py
# View component of Reversi game
#
# Copyright 2011, Rick Valenzano.
# All rights reserved.

import sys
from model import *

HUMAN_TYPE = 1
RANDOM_TYPE = 2
MINIMAX_TYPE = 3

# simple tuples with the part of the alphabet that we need
# LOWER_ALPHA allows for lower case entry as well
# Assumes board is no larger than 8x8
ALPHA = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'
LOWER_ALPHA = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'

# to help translate between a row entered as a char, and the corresponding int
row_equiv = {}
inverse_row_equiv = {}

# creates row_equiv and inverse_row_equiv
for num in range(BOARD_SIZE):
    row_equiv[ALPHA[num]] = num
    row_equiv[LOWER_ALPHA[num]] = num
    inverse_row_equiv[num] = ALPHA[num]

def move_inverter(move):
    return str(inverse_row_equiv[move[0]]) + str(move[1]+1)

# Prints out the legal moves of the given board
# board - the ReversiLogic object whose legal moves will be printed
def print_legal_moves(board):
    first = True
    for moves in board.legal_moves:
        #move_name = str(inverse_row_equiv[moves[0]]) + str(moves[1]+1)
        move_name = move_inverter(moves)
        if first:
            print(move_name, end="")
            first = False
        else:
            print(",", move_name, end="")
    print()
            
# Prints out the board and other game state information
# board - the ReversiLogic whose board will be printed
def print_board(board):
    
    print("   ", end="")
    for num in range(BOARD_SIZE):
        print(num + 1, end=" ")
    print()
    
    for row in range(BOARD_SIZE):
        print(ALPHA[row] + "  ", end="")
        #print(row, end=" ")
        for col in range(BOARD_SIZE):
            piece = board.occupied_by(row, col)
            if piece == WHITE:
                print("W ", end="")
            elif piece == BLACK:
                print("B ", end="")
            else:
                print(". ", end="")
                
        # print score and other game state info
        if row == BOARD_SIZE//2 - 1:
            print("  Score: ", end="")
            print("Black", board.num_chips(BLACK), end="")
            print(", White", board.num_chips(WHITE))
        elif row == BOARD_SIZE//2:
            if board.whose_turn() == WHITE:
                print("  It is white's turn to play")
            elif board.whose_turn() == BLACK:
                print("  It is black's turn to play")
            else:
                print()
        elif row == BOARD_SIZE//2 + 1 and board.whose_turn() != None:
            print("  Legal Moves: ", end="")
            print_legal_moves(board)
        else:
            print()

# Prints the help information
def print_help_info():
    print()
    print("The user can enter a move that is applicable to the current board.")
    print("The list of legal moves is shown beside the board.")
    print("The first character of the move refers to the row.")
    print("It can be entered in either lower or upper case.")
    print("The second character refers to the column.")
    print("The game ends when neither player can make a move.")
    print()
    print("The user can also enter 'seed' which will prompt the user for a")
    print("positive integer seed for the random number generator")
    print("In addition, the user can enter help, 'blackplayer',",
          "or 'whiteplayer'.")
    print("Entering 'blackplayer' allows the user to specify a computer agent")
    print("who to will act as the black player")
    print("Entering 'whiteplayer' works analogously.")

    print()

# Gets a move from the user
def get_user_move(user_input):
    
    if len(user_input) != 2:
        print("Invalid user input")
        return None

    row = row_equiv.get(user_input[0])
    if row == None:
        print("Invalid row:", row)
        return None
        
    # try and get column and catch integer input problems
    try:
        col = int(user_input[1]) - 1
    except ValueError:
        print("Invalid column: ", user_input[1])
        return None
    return (row, col)

# Gets a positive integer value from the user.
# Used to enter parameters for computer players
def get_pos_int_from_user(input_name):
    param_value = 0
    while True:
        print("Enter positive int value for", input_name, end="")
        user_input = input(": ").strip()
        
        try:
            param_value = int(user_input)
            if param_value <= 0:
                print("The value for", input_name, "must be bigger than 0")
                continue
            return param_value;
        
        except ValueError:
            print("Invalid value for", input_name, "entered")
    
    return None

# Gets information about the desired computer player
def get_player_info(name):
    player_type = 0;
    
    while True:
        print("Enter", name, "player type (human, random, or minimax)", 
              end="")
        user_input = input(": ").strip()
        
        if user_input == "human":
            return (HUMAN_TYPE, None)
        elif user_input == "random":
            return (RANDOM_TYPE, None)
        elif user_input == "minimax":
            # Gets the depth to which to perform minimax
            depth = get_pos_int_from_user("minimax depth")
            return (MINIMAX_TYPE, [depth])
        else:
            print("Invalid player type.")
            print("Input must either be human, random, or minimax")
        
    return None
    
