from Piece.Piece import Piece


class King(Piece):

    def can_move(self, position, board):
        return True