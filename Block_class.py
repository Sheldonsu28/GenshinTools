from __future__ import annotations
from typing import List


class BlockUnit:
    def __init__(self, facing, max_facing):
        self.coordinated_blocks = []
        self.curr_facing = facing
        self.max_facing = max_facing

    def turn(self, propagate=False):
        self.curr_facing = (self.curr_facing + 1) % self.max_facing
        if propagate:
            for block in self.coordinated_blocks:
                block.turn()

    def reset(self, value: int):
        self.curr_facing = value

    def set_coord(self, coord_blocks: List[BlockUnit]):
        self.coordinated_blocks = coord_blocks
