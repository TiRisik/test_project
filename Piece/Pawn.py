from Piece.Piece import Piece
from Ceil import Ceil

    def can_move(self, position, board):
        if self.y == 1:
            if position.y - self.y == 1 or position.y - self.y == 2:
                opponent = board.get_figure(Ceil(position.x, position.y))
                if opponent:
                    if opponent.x == position.x and opponent.y == position.y:
                        return True
                    if self.color == opponent.color:
                        return False
                    if self.color != opponent.color:
                        return False
                    if position.x - self.x == 0:
                        return False
                return True
        else:
            if position.y - self.y == 1 and position.x - self.x == 0:
                opponent = board.get_figure(Ceil(position.x, position.y))
                if opponent:
                    if self.color == opponent.color:
                        return False
                    if self.color != opponent.color:
                        return False
                return True
        if self.y == 6:
            if position.y - self.y == -1 and position.x - self.x == 0 or  position.y - self.y == -2 and position.x - self.x == 0:
                opponent = board.get_figure(Ceil(position.x, position.y))
                if opponent:
                    if opponent.y != 5:
                        return False
                    if self.color == opponent.color:
                        return False
                    if self.color != opponent.color:
                        return False
                return True
        else:
            if position.y - self.y == -1 and position.x - self.x == 0:
                opponent = board.get_figure(Ceil(position.x, position.y))
                if opponent:
                    if self.color == opponent.color:
                        return False
                    if self.color != opponent.color:
                        return False
                return True

