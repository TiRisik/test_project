from Piece.Castle import Castle
from Piece.King import King
from Piece.Queen import Queen
from Piece.Knight import Knight
from Piece.Bishop import Bishop
from Piece.Pawn import Pawn
from Ceil import Ceil

black_piece = [Castle("black_castle.png", 'BLACK'), Knight("black_knight.png", 'BLACK'), \
               Bishop("black_bishop.png", 'BLACK'), Queen("black_queen.png", 'BLACK'), \
               King("black_king.png", 'BLACK'), Bishop("black_bishop.png", 'BLACK'), \
               Knight("black_knight.png", 'BLACK'), Castle("black_castle.png", 'BLACK')]
white_piece = [Castle("white_castle.png", 'WHITE'), Knight("white_knight.png", 'WHITE'), \
               Bishop("white_bishop.png", 'WHITE'), Queen("white_queen.png", 'WHITE'), \
               King("white_king.png", 'WHITE'), Bishop("white_bishop.png", 'WHITE'), \
               Knight("white_knight.png", 'WHITE'), Castle("white_castle.png", 'WHITE')]


class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.board = [[None] * 8 for _ in range(8)]
        self.left = 0
        self.top = 0
        self.cell_size = 100
        for i in range(2):
            if not i:
                white_chess = [Pawn('white_pawn.png', 'WHITE') for i in range(8)]
                black_chess = black_piece.copy()
            else:
                white_chess = white_piece.copy()
                black_chess = [Pawn('black_pawn.png', 'BLACK') for i in range(8)]
            for j in range(8):
                self.add_figure(black_chess[j], Ceil(j, i))
                self.add_figure(white_chess[j], Ceil(j, 6 + i))

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
