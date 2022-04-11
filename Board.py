from __future__ import annotations
from Block_class import BlockUnit
from typing import List
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


# A, B
# C, D

#   0
# 1   3
#   2


if __name__ == "__main__":
    a = BlockUnit(1, 3)
    b = BlockUnit(2, 3)
    c = BlockUnit(0, 3)
    d = BlockUnit(0, 3)
    e = BlockUnit(2, 3)

    l = [a, b, c, d, e]
    a.set_coord([b])
    b.set_coord([a, c])
    c.set_coord([b, d])
    d.set_coord([c, e])
    e.set_coord([d])

    init_state = extract_states(l)
    term = [0, 0, 0, 0, 0]

    board = Board(l, term)

    sol = board.solve()

    reset_states(l, init_state)

    print(verifier(l, sol, term))


