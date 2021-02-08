from Ceil import Ceil
from Piece.Piece import Piece


class Knight(Piece):

    def can_move(self, position, board):
        if (abs(position.x - self.x) == 2 or abs(position.y - self.y) == 2)\
               and (abs(position.x - self.x) == 1 or abs(position.y - self.y) == 1):
            opponent = board.get_figure(Ceil(position.x, position.y))
            if opponent:
                if self.color == opponent.color:
                    return False
                else:
                    if opponent.x != position.x or opponent.y != position.y:
                        return False
            return True
        return False