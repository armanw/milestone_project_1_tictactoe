from typing import Any

import numpy as np
from tomlkit import string


class Board:
    def __init__(self):
        self.matrix = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], dtype=np.str_)

    def put_symbol(self, symbol: str, row_x: int, column_y: int):
        # symbol - x or o
        # row_x - 1 -3, column_y - 1-3

        self.matrix[row_x-1][column_y-1] = symbol

    def get_symbol_at(self, row_x: int, column_y: int) -> np.ndarray[Any, np.dtype[np.str_]]:
        return self.matrix[row_x-1][column_y-1]

    def is_full(self):
        return ' ' not in self.matrix

    def has_3_in_line(self):
        potential_matches = []
        # checking rows:
        potential_matches.append(self.matrix[0, :])
        potential_matches.append(self.matrix[1, :])
        potential_matches.append(self.matrix[2, :])

        # checking columns:
        potential_matches.append(self.matrix[:, 0])
        potential_matches.append(self.matrix[:, 1])
        potential_matches.append(self.matrix[:, 2])

        # checking diagonal:
        potential_matches.append(np.diag(self.matrix))
        # checking anti-diagonal:
        potential_matches.append(np.fliplr(self.matrix).diagonal())

        # check if same 3 in line
        line_states = [
            line[0] != ' '
            and line[0] == line[1]
            and line[1] == line[2]
            for line in potential_matches
        ]
        # if any is true, return true
        return any(line_states)


