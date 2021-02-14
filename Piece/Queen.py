from Ceil import Ceil
from Piece.Piece import Piece


class Queen(Piece):
    def check_diagonal(self, position, board):
        if figure := board.get_figure(Ceil(position.x, position.y)):
            if self.is_same(figure.color):
                return False
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

    def check_castle(self, equal, first, second, number, board, position):
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
            return self.check_castle(self.x, position.y, self.y, 1, board, position)
        elif position.y == self.y:
            return self.check_castle(self.y, position.x, self.x, 2, board, position)
        elif position.x != self.x and position.y != self.y:
            if abs(position.x - self.x) == abs(position.y - self.y):
                return self.check_diagonal(position, board)
        return False