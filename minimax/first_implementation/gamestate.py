from copy import deepcopy

rows = 2
columns = 3

class GameState:

    def __init__(self):
        self._board = [[0 for x in range(rows)] for y in range(columns)]
        self._board[-1][-1] = 1
        self._parity = 0
        self._player_locations = [None, None]

    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.

        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
        """
        pass

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
        pass

    def get_empty_spaces(self):
        """Returns a list with the indices of 0 values as coordinates."""
        return [(x, y) for y in range(rows) for x in range(columns) if self._board[x][y] == 0]

import code; code.interact(local=dict(globals(), **locals()))
