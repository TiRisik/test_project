from Piece.Piece import Piece
from Ceil import Ceil
#hello


class Bishop(Piece):
    def check_diagonal(self, position, board):
        dx = 1 if position.x > self.x else -1
        dy = 1 if position.y > self.y else -1
        tx, ty = self.x + dx, self.y + dy
        while (tx != position.x) and (ty != position.y):
            figure = board.get_figure(Ceil(tx, ty))
            if figure and tx != position.x and ty != position.y:
                return False
            tx += dx
            ty += dy
        return True


    def can_move(self, position, board):
        if position.x != self.x and position.y != self.y:
            if abs(position.x - self.x) == abs(position.y - self.y):
                return self.check_diagonal(position, board)
        return False
