import pygame
import os


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
white_coordinate = {}
black_coordinate = {}


def draw_letters_and_numbers(screen):
    font = pygame.font.Font(None, 30)
    k, k1 = 0, 1
    for i in range(2):
        if i:
            texts = letters.copy()
            x, y = 80, 780
        else:
            texts = numbers.copy()
            x, y = 5, 5
        for j in range(8):
            text = font.render(str(texts[j]), True, pygame.Color('black'))
            text_x = x + j * 100 * k
            text_y = y + j * 100 * k1
            screen.blit(text, (text_x, text_y))

        k, k1 = 1, 0


class ImageChess:
    global white_coordinate, black_coordinate

    def __init__(self):
        self.white_king = pygame.transform.scale(load_image("white_king.png"), (80, 80))
        self.white_queen = pygame.transform.scale(load_image("white_queen.png"), (80, 80))
        self.white_bishop = pygame.transform.scale(load_image("white_bishop.png"), (80, 80))
        self.white_castle = pygame.transform.scale(load_image("white_castle.png"), (60, 80))
        self.white_knight = pygame.transform.scale(load_image("white_knight.png"), (80, 80))
        self.black_king = pygame.transform.scale(load_image("black_king.png"), (80, 80))
        self.black_queen = pygame.transform.scale(load_image("black_queen.png"), (80, 80))
        self.black_bishop = pygame.transform.scale(load_image("black_bishop.png"), (80, 80))
        self.black_castle = pygame.transform.scale(load_image("black_castle.png"), (60, 80))
        self.black_knight = pygame.transform.scale(load_image("black_knight.png"), (80, 80))
        self.white_pawn = pygame.transform.scale(load_image("white_pawn.png"), (60, 80))
        self.black_pawn = pygame.transform.scale(load_image("black_pawn.png"), (60, 80))
        self.white_chess = [self.white_castle, self.white_knight, self.white_bishop, self.white_queen, \
                            self.white_king, self.white_bishop, self.white_knight, self.white_castle]
        self.black_chess = [self.black_castle, self.black_knight, self.black_bishop, self.black_queen, \
                            self.black_king, self.black_bishop, self.black_knight, self.black_castle]
        for i in range(2):
            if i:
                white_figure = [self.white_pawn for i in range(8)]
                black_figure = self.black_chess.copy()
            else:
                black_figure = [self.black_pawn for i in range(8)]
                white_figure = self.white_chess.copy()
            for j in range(8):
                white_coordinate[(j, i)] = [white_figure[j], (j, i)]
                black_coordinate[(j, 6 + i)] = [black_figure[j], (j, 6 + i)]

    def select_photo(self, screen):
        for i in white_coordinate:
            screen.blit(white_coordinate[i][0], (white_coordinate[i][1][0] * 100 + 15,\
                                                 white_coordinate[i][1][1] * 100 + 15))
        for j in black_coordinate:
            screen.blit(black_coordinate[j][0], (black_coordinate[j][1][0] * 100 + 10, \
                                                 black_coordinate[j][1][1] * 100 + 10))

    def update(self, active_chess, coordinate_chess):
        if active_chess in white_coordinate:
            white_coordinate[coordinate_chess] = [white_coordinate[active_chess][0], coordinate_chess]
            del white_coordinate[active_chess]
        elif active_chess in black_coordinate:
            black_coordinate[coordinate_chess] = [black_coordinate[active_chess][0], coordinate_chess]
            del black_coordinate[active_chess]


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 100

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                x = self.left
                y = self.top
                lens = self.cell_size
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    pygame.draw.rect(screen, (255, 255, 255), (x + 1, y + 1, lens - 2, lens - 2), 0)
                    pygame.draw.rect(screen, (0, 0, 0), (x, y, lens, lens), 1)
                else:
                    pygame.draw.rect(screen, (31, 20, 10), (x, y, lens, lens), 0)
                self.left = x + lens
            self.left = self.left - self.cell_size * len(self.board[i])
            self.top = self.top + self.cell_size
        self.top = self.top - self.cell_size * len(self.board)

    def get_coordinate(self, mouse_pos):
        x, y = mouse_pos
        x1 = (x - self.left) // self.cell_size
        y1 = (y - self.top) // self.cell_size
        coordinate = (x1, y1)
        return coordinate
