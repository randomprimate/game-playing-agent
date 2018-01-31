# The Alpha Beta Search Algorithm

![alpha-beta](assets/alpha-beta-search.png)

This video introduces the concept of alpha-beta pruning which modifies the minimax algorithm by introducing two new variables: α -- the maximum lower bound of the minimax value -- and β -- the minimum upper bound of the minimax value. In other words: at every state in the game tree α represents the guaranteed worst-case score that the MAX player could achieve, and β represents the guaranteed worst-case score that the MIN player could achieve.

The estimates of α are only updated in each MAX node, while β is only updated in each MIN node. If the estimate of the upper bound is ever lower than the estimate of the lower bound in any state, then the search can be cut off because there are no values between the upper and lower bounds. Practically this means that your agent could do better by making a different move earlier in the game tree to avoid the pruned state.

Implementing alpha-beta pruning in minimax only adds the two new variables (alpha & beta), and adds a conditional branch to the MIN and MAX nodes to break and return the appropriate bound when a state is pruned. (See the pseudocode above & compare with the [minimax](https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md) algorithm.)

There's one more difference you'll notice between minimax and alpha-beta: the alpha-beta search function seems to call the `max_value()` helper from the root node, while minimax calls the `min_value()` helper. But the pseudocode for alpha-beta search is just hiding some additional complexity: calling `max_value()` returns the score of the best branch -- but it doesn't tell you what the best branch is. You can implement the algorithm just like the minimax-decision function if you modify it to update alpha between branches.
