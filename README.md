# game-playing-agent
Isolation game playing agent

## Description and Notes

### Board.
A 3x2 board is used in these examples. The board is a list such as `[[0,0], [0,0], [0,0]]`
which can be visualized as:

```
| 0 | 0 | 0 |
-------------
| 0 | 0 | 0 |
```

To represent a box in the board we use tuples. The tuple `(1, 0)` would be
equivalent to `[[0,0], [1,0], [0,0]]` and can be visualized like so
```
| 0 | 1 | 0 |
-------------
| 0 | 0 | 0 |
```

### Two Dimensional Movement
*  **Horizontal:** Coordinate changes only on the first element of the tuple.
*  **Vertical:** Coordinate changes only on the second element of the tuple.
*  **Diagonal:** Unitary coordinate changes for both elements of the tuple.

## Troubleshooting
Place this line whenever you need to interrupt the process and bring up a console,
just like `binding.pry` in Ruby.
```
import code; code.interact(local=dict(globals(), **locals()))
```

## Install

* Python 3
* No dependencies