from Ceil import Ceil
from Piece.Piece import Piece


class Queen(Piece):
    def check_bishop(self, first, second, third, fourth, board):
        if first < second and third < fourth:
            i1, i2 = first, second
            j1, j2 = third, fourth
        elif first > second and third < fourth:
            i1, i2 = second + 1, first + 1
            j1, j2 = third, fourth
        elif first < second and third > fourth:
            i1, i2 = first, second
            j1, j2 = fourth + 1, third + 1
        elif first > second and third > fourth:
            i1, i2 = second + 1, first + 1
            j1, j2 = fourth + 1, third + 1
        for i in range(i1, i2):
            for j in range(j1, j2):
                opponent = board.get_figure(Ceil(i, j))
                if opponent:
                    if self.color == opponent.color:
                        return False
                    else:
                        if opponent.x != first or opponent.y != third:
                            return False
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
                return self.check_bishop(position.x, self.x, position.y, self.y, board)
        return False