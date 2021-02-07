from MarkAntonovich.Castle import Castle
from MarkAntonovich.Ceil import Ceil


class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.board = [[None] * 8 for _ in range(8)]
        self.left = 0
        self.top = 0
        self.cell_size = 100
        self.add_figure(
            Castle("black_castle.png", 'BLACK'),
            Ceil(3, 4)
        )

    def add_figure(self, figure, position):
        self.board[position.x][position.y] = figure
        figure.x, figure.y = position.x, position.y

    def get_figure(self, position):
        return self.board[position.x][position.y]

    def get_board(self):
        return self.board

    def move_figure(self, figure, to_position):
        previous_x, previous_y = figure.x, figure.y
        figure.move(to_position)
        self.board[previous_x][previous_y] = None
        self.board[figure.x][figure.y] = figure
