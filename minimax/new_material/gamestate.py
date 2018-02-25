#!/usr/bin/python

from copy import deepcopy
import array_handling as ah

rows = 2
columns = 3
elements = [0] * columns

class GameState:

    def __init__(self):
        """The GameState class constructor performs required
        initializations when an instance is created.
        Parameters
        ----------
        self:
            instance methods automatically take "self" as an
            argument in python

        Returns
        -------
        None
        """
        self.board = ah.create_matrix(rows, columns, elements)
        self.board[2][1] = 1
        self.player_state = {
            "player_1": [1, ()],
            "player_2": [0, ()]
        }

    def update_player_position(self, move):
        if(self.player_state["player_1"][0] == 1):
            self.player_state["player_1"][1] = move
        else:
            self.player_state["player_2"][1] = move


    def switch_turn(self):
        if(self.player_state["player_1"][0] == 1):
            self.player_state["player_1"][0] = 0
            self.player_state["player_2"][0] = 1
        else:
            self.player_state["player_1"][0] = 1
            self.player_state["player_2"][0] = 0

    def first_move(self):
        moves = []
        for i, n in enumerate(self.board):
            for ix, nu in enumerate(n):
                # Check if available
                if(nu == 0):
                    moves.append((i, ix))
        return moves

    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """
        moves = []
        if(self.player_state["player_1"][0] == 1):
            player_location = self.player_state["player_1"][1]
        else:
            player_location = self.player_state["player_2"][1]

        if(len(player_location) == 0):
            moves = self.first_move()
        else:
            moves = ah.index_available_matrix_elements(columns, self.board, player_location)

        return moves


    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.

        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
            (e.g., (0, 0) if the active player will move to the
            top-left corner of the board)
        """
        if move not in self.get_legal_moves():
            raise RuntimeError("Attempted forecast of illegal move")
        new_state = deepcopy(self)
        new_state.board[move[0]][move[1]] = 1
        new_state.update_player_position(move)
        new_state.switch_turn()

        return new_state


    def print_coordinates(self):
        """ Print the coordinates of the board
        with the current value.
        """
        for i, n in enumerate(self.board):
            for ix, nu in enumerate(n):
                print("(" + str(i) + ", " + str(ix) + ") = " + str(nu))


if __name__ == "__main__":
    # This code is only executed if "gameagent.py" is the run
    # as a script (i.e., it is not run if "gameagent.py" is
    # imported as a module)
    emptyState = GameState()  # create an instance of the object
