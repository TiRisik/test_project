from Piece.Piece import Piece
from Ceil import Ceil


class Castle(Piece):
    def check(self, equal, first, second, number, board, position):
        if first < second:
            i1, i2 = first, second
        else:
            i1, i2 = second + 1, first + 1
        for i in range(i1, i2):
            if number == 1:
                opponent = board.get_figure(Ceil(equal, i))
            else:
                opponent = board.get_figure(Ceil(i, equal))
            if opponent:
                if self.color == opponent.color:
                    return False
                else:
                    if opponent.x != position.x or opponent.y != position.y:
                        return False
        return True

    def can_move(self, position, board):
        if position.x == self.x:
            return self.check(self.x, position.y, self.y, 1, board, position)
        elif position.y == self.y:
            return self.check(self.y, position.x, self.x, 2, board, position)
        return False
