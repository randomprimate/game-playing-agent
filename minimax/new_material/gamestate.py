from copy import deepcopy

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
        # Create an empty board
        self.board = [[0, 0], [0, 0], [0, 0], [0, 0]]
        # 0 | 0 | 0
        # 0 | 0 | 0
        # Fill in lower right corner because ... why not
        self.board[2][1] = 1
        # 0 | 0 | 0
        # 0 | 0 | 1
        # player_1 [1, (1, 0)] Player 1's turn & current pos at (1, 0)
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


    def horizontal_moves(self, moves, player_location):
        hor = []
        pos = player_location
        # Set new array of horizontal available boxes
        for i in moves:
            if(i[1]==pos[1]):
                hor.append(i)

        # Remove available box if prior box (in between current box and original
        # position) is blocked
        for i, x in enumerate(hor):
            print(x)
            print(pos)
            #if(x[0] != 0): # may not be required
            # If current box is to the right of player's position
            if(x[0] > pos[0]):
                """
                If index of the current box minus the index of the prev box
                is greater than one it means there was a blocked box in
                between
                """
                print(hor)
                print(i)
                print(hor[i+1][0] - x[0])
                # Not immediately after current position
                """
                if((x[0] - pos[0]) != 1):
                    if((x[0] - hor[i+1][0]) > 1):
                        hor.remove(x)
                        moves.remove(x)
                """
            # If current box is to the left of player's position
            elif(x[0] < pos[0]):
                # While it's not the box exactly to the right of the
                # player's position
                if((x[0] - pos[0]) != 1):
                    if((hor[i-1][0] - x[0]) > 1):
                        hor.remove(x)
                        moves.remove(x)

        import code; code.interact(local=dict(globals(), **locals()))
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
        # If player's turn
        if(self.player_state["player_1"][0] == 1):
            player_location = self.player_state["player_1"][1]
        else:
            player_location = self.player_state["player_2"][1]
        # Check blocked and assign available moves
        for i, n in enumerate(self.board):
            for ix, nu in enumerate(n):
                # Check if available
                if(nu == 0):
                    moves.append((i, ix))
        # If first move
        if(len(player_location) != 0):
            moves = self.horizontal_moves(moves, player_location)

            # When applying vertical and diagonal check we only need to
            # keep removing the bloked boxes from moves

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
        #if move not in self.get_legal_moves():
        #    raise RuntimeError("Attempted forecast of illegal move")
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
