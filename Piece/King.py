from Piece.Piece import Piece
from Ceil import Ceil


class King(Piece):
    def can_move(self, position, board):
        if figure := board.get_figure(Ceil(position.x, position.y)):
            if self.is_same(figure.color):
                if figure.return_name() == 'Castle':
                    dx = 1 if position.x > self.x else -1
                    dx1 = 1 if position.x > self.x else 2
                    dx2 = 3 - dx1
                    board.add_figure(self, Ceil(position.x - dx * dx1, position.y))
                    board.board[self.x][self.y] = None
                    board.add_figure(figure, Ceil(position.x - dx * dx2, position.y))
                    board.board[position.x][position.y] = None
                return False
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

    def return_name(self):
        return 'King'
