from Piece.Piece import Piece
from Ceil import Ceil


class Castle(Piece):
    def check(self, position, board, x, y):
        if figure := board.get_figure(Ceil(position.x, position.y)):
            if self.is_same(figure.color):
                return False
        if x:
            dy = 1 if position.y > self.y else -1
            ty = self.y + dy
            while ty != position.y:
                figure = board.get_figure(Ceil(self.x, ty))
                if figure and ty != position.y:
                    return False
                ty += dy
            return True
        if y:
            dx = 1 if position.x > self.x else -1
            tx = self.x + dx
            while tx != position.x:
                figure = board.get_figure(Ceil(tx, self.y))
                if figure and tx != position.x:
                    return False
                tx += dx
            return True

    def can_move(self, position, board):
        if position.x == self.x:
            return self.check(position, board, True, False)
        elif position.y == self.y:
            return self.check(position, board, False, True)
        return False
