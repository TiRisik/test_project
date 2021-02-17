from Piece.Piece import Piece
from Ceil import Ceil


class Pawn(Piece):
    START_ROW = {
        'WHITE': 6,
        'BLACK': 1
    }
    MOVE_DIRECTION = {
        'WHITE': -1,
        'BLACK': 1
    }

    def can_move(self, position, board):
        figure_on_position = board.get_figure(Ceil(position.x, position.y))
        if figure_on_position:
            if not self.is_same(figure_on_position.color):
                if abs(self.x - position.x) == 1 and (self.y + self.MOVE_DIRECTION[self.color] == position.y):
                    return True
            else:
                return False
        if self.y == self.START_ROW[self.color]:
            return (self.y + 2 * self.MOVE_DIRECTION[self.color] == position.y and self.x == position.x) or \
                   (self.y + self.MOVE_DIRECTION[self.color] == position.y and self.x == position.x)
        else:
            return self.y + self.MOVE_DIRECTION[self.color] == position.y and self.x == position.x

    def transformation_pawn(self):
        if self.y == 7 or self.y == 0:
            return True
        return False
