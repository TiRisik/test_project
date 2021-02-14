from Piece.Piece import Piece
from Ceil import Ceil


# b.__class__.__name__


class King(Piece):
    def can_move(self, position, board):
        if position.y - self.y == 1 or position.x - self.x == -1:
            opponent = board.get_figure(Ceil(position.x, position.y))
            if opponent:
                if self.color == opponent.color:
                    return False
            return True
        if position.y - self.y == -1 or position.x - self.x == 1:
            opponent = board.get_figure(Ceil(position.x, position.y))
            if opponent:
                if self.color == opponent.color:
                    return False
            return True
