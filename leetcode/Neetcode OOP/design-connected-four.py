from __future__ import annotations

import enum
from typing import List
from functools import cached_property


class PlacementError(BaseException):
    # raised if placing column is out of bounds or full
    pass


class Color(enum.Enum):
    EMPTY = 0
    RED = 1
    YELLOW = 2
    ORANGE = 3


class ConnectedX:
    def __init__(self, x=4, players=2, color=[Color.RED, Color.YELLOW], dimensions=(6, 7)):
        self.x = x
        self.players = 2
        self.color = color
        self.rows = dimensions[0]
        self.cols = dimensions[1]
        self.board = self._init_board()

    def _init_board(self) -> List[List[Color]]:
        return [[Color.EMPTY]*self.cols for _ in range(self.rows)]

    @cached_property
    def check_vertical(self, player: Color):
        # TODO
        pass

    @cached_property
    def check_horizontal(self, player: Color):
        # TODO
        pass

    @cached_property
    def check_diagonal(self, player: Color):
        # TODO
        pass

    @cached_property
    def check_connect(self, player: Color) -> bool:
        return self.check_vertical(player) or self.check_horizontal(player) or self.check_diagonal(player)

    @cached_property
    def check_win(self) -> Color | None:
        for c in self.color:
            if self.check_connect(c):
                return c

    @cached_property
    def placed_row(self, col) -> int: # return the row of the current placement, returning self.rows if out of bounds
        for row in range(self.rows):
            if self.board[row][col] == Color.EMPTY: # check if (row, col) is occupied by either player
                return row
        return self.rows

    def place_piece(self, player: Color, col: int) -> None:
        # if out of bounds or full
        if not 0 <= col < self.cols:
            print("Column is out of bounds!")
            raise PlacementError

        row = self.placed_row(col)
        if row == self.rows:
            print("Column is full!")
            raise PlacementError

        self.board[row][col] = player









