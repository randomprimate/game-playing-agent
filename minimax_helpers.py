import settings

def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    settings.call_counter += 1
    moves_available = bool(gameState.get_legal_moves())

    return not moves_available


def min_value(gameState, depth):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    #import code;code.interact(local=dict(globals(), **locals()))

    if terminal_test(gameState):
        return 1

    if depth <= 0:
        return 0

    v = float("inf")
    # Values for all moves from the current level
    for m in gameState.get_legal_moves():
        v = min(v, max_value(gameState.forecast_move(m), depth - 1))
    return v


def max_value(gameState, depth):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return -1

    if depth <= 0:
        return 0

    v = float("-inf")
    # Values for all moves from the current level
    for m in gameState.get_legal_moves():
        v = max(v, min_value(gameState.forecast_move(m), depth - 1))
    return v
