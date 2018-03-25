import minimax_helpers
from gamestate import *

print("Creating empty game board...")
g = GameState()

print("Calling min_value on an empty board...")
v = minimax_helpers.min_value(g)

if v == -1:
    print("min_value() returned the expected score!")
else:
    print("Uh oh! min_value() did not return the expected score.")


import code; code.interact(local=dict(globals(), **locals()))

print("Getting legal moves for player 1...")
p1_empty_moves = g.get_legal_moves()
print("Found {} legal moves.".format(len(p1_empty_moves or [])))

print("Applying move (0, 0) for player 1...")
g1 = g.forecast_move((0, 0))

print("Getting legal moves for player 2...")
p2_empty_moves = g1.get_legal_moves()
if (0, 0) in set(p2_empty_moves):
    print("Failed\n  Uh oh! (0, 0) was not blocked properly when " +
          "player 1 moved there.")

print("Applying move (1, 0) for player 2...")
g2 = g1.forecast_move((1, 0))

print("Getting legal moves for player 1...")
p1_empty_moves_g2 = g2.get_legal_moves()
if (2, 0) in set(p1_empty_moves_g2):
    print("Failed\n  Uh oh! (2, 0) was not blocked properly when " +
          "player 2 moved to (1, 0).")
else:
    print("Everything looks good!")
