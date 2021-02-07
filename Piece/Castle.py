from Piece.Piece import Piece


class Castle(Piece):

    def can_move(self, position):
        return position.x == self.x or position.y == self.y
