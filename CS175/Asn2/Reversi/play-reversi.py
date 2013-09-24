import model
import view


class Game(object):
    def __init__(self, board):
        self.state = model.ReversiLogic()
        self.board = board
    
    def play(self):
        view.new_game_message()
        # Draw the lines and starting pieces on the board.
        self.board.create()
        # Loop until a player quits or the game ends.
        while 1:
            color = self.state.get_whose_turn()
            # If color is None, the game logic could not find a legal move.
            if not color:
                self.game_over()
                # Allow the user to play another game.
                return view.get_play_again()
            # Get the player's move.
            action = view.get_user_input(color)
            if action == 'quit':
                # Though the user quit the game, allow him to start a new one.
                return view.get_play_again()
            self.make_move(action[0], action[1])
    
    # Determine if the user's move is a legal one, and if it is,
    # update both the state's board and the graphical board.
    def make_move(self, row, col):
        # squares is a list of Square objects, each of which needs to
        # be changed as a result of the current move.
        squares = self.state.make_move(row, col)
        # If the list is empty, it was an invalid move.
        if not squares:
            view.error_message('move')
        # If the move was legal, the state has already been updated.
        # Only the graphical board needs to be updated now.
        else:
            self.board.change_squares(squares)
    
    # Get the number of pieces for each side, determine a 
    # winner, and show the results.
    def game_over(self):
        white_score = self.state.count_pieces('w')
        view.show_score('w', white_score)
        black_score = self.state.count_pieces('b')
        view.show_score('b', black_score)
        if white_score > black_score: winner = 'w'
        elif white_score < black_score: winner = 'b'
        else: winner = None
        view.show_winner(winner)


if __name__ == '__main__':
    view.welcome_message()
    # The board instance communicates with the graphical representation of
    # the board through Sketchpad.jar.
    board = view.Board()
    # Loop until the user no longer wants to play any more games.
    while 1:
        game = Game(board)
        # If game.play() returns false, the user chose not to play any more.
        if not game.play():
            view.exit_message()
            game.board.delete()
            break
    
    