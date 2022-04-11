from Block_class import BlockUnit

from typing import List
from typing import Union
import numpy as np


def solve_blocks_dfs(blocks: List[BlockUnit], terminate_cond: List[int], seen_state) -> Union[List[int], None]:
    initial_state = [b.curr_facing for b in blocks]

    if initial_state == terminate_cond:
        return []

    if str(initial_state) in seen_state:
        return None

    seen_state[str(initial_state)] = True

    for i in range(len(blocks)):
        blocks[i].turn(propagate=True)
        termination = solve_blocks_dfs(blocks, terminate_cond, seen_state)
        if termination is not None:
            return [i] + termination

        for j in range(len(blocks)):
            blocks[j].reset(initial_state[j])

    return None


def solve_blocks_bfs(blocks: List[BlockUnit], terminate_cond: List[int], seen_state) -> Union[List[int], None]:
    """
    BFS with backtracking
    :param blocks: List of blocks
    :param terminate_cond: Condition to be satisfied
    :param seen_state: States seen by the algorithm before
    :return: sequence blocks to interact if solution is found.
    """
    init_state = [b.curr_facing for b in blocks]
    queue = [init_state]
    seen_state[str(init_state)] = []
    counter = 0
    sol = None

    while len(queue) > 0:
        curr_state = queue.pop(0)
        reset_states(blocks, curr_state)
        for i in range(len(blocks)):
            blocks[i].turn(propagate=True)
            new_state = extract_states(blocks)
            if new_state == terminate_cond:
                sol = seen_state[str(curr_state)] + [i]
                return sol
            if str(new_state) not in seen_state:
                seen_state[str(new_state)] = seen_state[str(curr_state)] + [i]
                queue += [new_state]
            reset_states(blocks, curr_state)
        counter += 1
    return sol


def reset_states(blocks, states):
    for j in range(len(blocks)):
        blocks[j].reset(states[j])


def extract_states(blocks):
    return [b.curr_facing for b in blocks]


def verifier(blocks, operation, terminate_cond):
    for i in operation:
        blocks[i].turn(propagate=True)
    result = extract_states(blocks)
    return terminate_cond == result


if __name__ == "__main__":
    a = np.array([[3, 1, -1, 2],
                  [-5, 1, 3, -4],
                  [2, 0, 1, -1],
                  [1, -5, 3, -3]])
    b = np.array([[2, 1, -1],
                  [4, -1, 1],
                  [201, 102, -99]])
    print(np.linalg.det(b))
