from typing import Tuple, Iterator

import math


def get_checker_pattern(init_offset: int, init_row: int, rows: int, max_col: int) -> Iterator[Tuple[int, int]]:
    """
    :returns: A generator returning (row, column)
    """
    times_per_col = math.ceil(max_col / 2)
    offset = init_offset
    for piece_row in range(rows):
        for piece_col_index in range(times_per_col):
            row = piece_row + init_row
            col = piece_col_index * 2 + offset

            yield (row, col)

        if offset == 0:
            offset = 1
        else:
            offset = 0
