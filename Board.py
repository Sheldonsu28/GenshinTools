from __future__ import annotations
from Algorithms import *


class Board:
    def __init__(self, blocks: List[BlockUnit], termination_condition: List[int]):
        self.blocks = blocks
        self.terminate_cond = termination_condition
        self.states = {}

    def solve(self):
        result = solve_blocks_bfs(self.blocks, self.terminate_cond, self.states)
        if result is not None:
            print(result)
            return result


if __name__ == "__main__":

    # 5 blocks, all of them have 3 possible states
    # block 'a' is currently at state 1 (second state), 'b' at state 2 (third state) etc
    a = BlockUnit(1, 3)
    b = BlockUnit(2, 3)
    c = BlockUnit(0, 3)
    d = BlockUnit(0, 3)
    e = BlockUnit(2, 3)

    blocks = [a, b, c, d, e]

    # Set linking, state change of 'a' will trigger state change of b
    # State change of b will trigger state change of a and c. etc
    a.set_link([b])
    b.set_link([a, c])
    c.set_link([b, d])
    d.set_link([c, e])
    e.set_link([d])

    term = [0, 0, 0, 0, 0]

    board = Board(blocks, term)

    sol = board.solve()

    if sol is None:
        print('No solutions found')


