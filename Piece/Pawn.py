from Piece.Piece import Piece


class Pawn(Piece):

    def can_move(self, position, board):
        return True