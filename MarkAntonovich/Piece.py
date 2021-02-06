class Piece:
    def __init__(self, image, color):
        self.x = None
        self.y = None
        self.image = image
        self.color = color
        pass

    def is_same(self, color):
        return self.color == color

    def move(self, position):
        if self.can_move(position):
            self.x = position.x
            self.y = position.y

    def get_image(self):
        return self.image

    def can_move(self, position):
        pass
