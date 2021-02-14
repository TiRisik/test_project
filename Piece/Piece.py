class Piece:
    def __init__(self, image, color):
        self.x = None
        self.y = None
        self.image = image
        self.color = color

    def is_same(self, color):
        return self.color == color

    def move(self, position, board):
        if self.can_move(position, board):
            self.x = position.x
            self.y = position.y

    def get_image(self):
        return self.image

    def can_move(self, position, board):
        pass

    def transformation_pawn(self):
        return False
