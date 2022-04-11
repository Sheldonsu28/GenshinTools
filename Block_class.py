from __future__ import annotations
from typing import List


class BlockUnit:

    def __init__(self, facing, max_facing):
        """
        Initialize a block
        :param facing: Current facing/state of the block 0-indexed
        :param max_facing: Number of possible facing of the block
        """
        self.linked_blocks = []
        self.curr_facing = facing
        self.max_facing = max_facing

    def turn(self, propagate=False):
        """
        Turn / change the state of current block
        :param propagate: Propagate action to linked blocks
        :return: None
        """
        self.curr_facing = (self.curr_facing + 1) % self.max_facing
        if propagate:
            for block in self.linked_blocks:
                block.turn()

    def reset(self, value: int):
        """
        Reset current facing
        :param value: The state / facing you want to set, 0 <= value < max_facing
        :return: None
        """
        self.curr_facing = value

    def set_link(self, linked_blocks: List[BlockUnit]):
        """
        Set the blocks to link with current block
        :param linked_blocks: List of block that is linked to this block
        :return: None
        """
        self.linked_blocks = linked_blocks
