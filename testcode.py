import minimax_helpers
import minimax
from gamestate import *

print("\nCreating empty game board...")
g = GameState()

"""
 Testing minimax_helpers
"""
print("\nTesting minimax_helpers:")
print("- Calling min_value on an empty board...")
v = minimax_helpers.min_value(g)

if v == -1:
    print("OK: min_value() returned the expected score!\n")
else:
    print("ERR: Uh oh! min_value() did not return the expected score.\n")

print("\nTesting GameState:")
print("- Getting legal moves for player 1...")
p1_empty_moves = g.get_legal_moves()
print("- Found {} legal moves.".format(len(p1_empty_moves or [])))

print("- Applying move (0, 0) for player 1...")
g1 = g.forecast_move((0, 0))

print("- Getting legal moves for player 2...")
p2_empty_moves = g1.get_legal_moves()
if (0, 0) in set(p2_empty_moves):
    print("ERR: Failed\n  Uh oh! (0, 0) was not blocked properly when " +
          "player 1 moved there.\n")

print("- Applying move (1, 0) for player 2...")
g2 = g1.forecast_move((1, 0))

print("- Getting legal moves for player 1...")
p1_empty_moves_g2 = g2.get_legal_moves()
if (2, 0) in set(p1_empty_moves_g2):
    print("ERR: Failed\n  Uh oh! (2, 0) was not blocked properly when " +
          "player 2 moved to (1, 0).\n")
else:
    print("OK: Everything looks good!\n")

"""
 Testing Minimax Algorithm
"""
print("Testing Minimax Algorithm:")

best_moves = {(0, 0), (2, 0), (0, 1)}
rootNode = GameState()
minimax_move = minimax.minimax_decision(rootNode)

print("- Best move choices: {}".format(list(best_moves)))
print("- Your code chose: {}".format(minimax_move))

if minimax_move in best_moves:
    print("OK: That's one of the best move choices. Looks like your minimax-decision function worked!\n")
else:
    print("ERR: Uh oh...looks like there may be a problem.\n")
