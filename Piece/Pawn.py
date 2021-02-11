from Piece.Piece import Piece
from Ceil import Ceil

class Pawn(Piece):

    def can_move(self, position, board):
        if position.y - self.y == 1 and position.x - self.x == 0 or position.y - self.y == 2 and position.x - self.x == 0:
            opponent = board.get_figure(Ceil(position.x, position.y))
            if opponent:
                if opponent.y - position.y == 1 or opponent.y - position.y == -1:
                    return False
                if self.color == opponent.color:
                    return False
                if self.color != opponent.color:
                    return False
            return True
        if position.y - self.y == -1 and position.x - self.x == 0 or  position.y - self.y == -2 and position.x - self.x == 0:
            opponent = board.get_figure(Ceil(position.x, position.y))
            if opponent:
                if position.y :
                    return False
                if self.color == opponent.color:
                    return False
                if self.color != opponent.color:
                    return False
            return True
