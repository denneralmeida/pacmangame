import pygame

score = 18
coins = []


class Pacman:
    global coins
    x_pos, y_pos, = 1, 1

    def __init__(self):
        self.map = Maze()
        self.score = 0
        self.winner = False
        pygame.mixer.init()
        self.song = pygame.mixer.Sound('sounds/eat.wav')
        self.player = pygame.image.load('images/pacman-right.png')

    def move_up(self):
        self.rotate('up')
        if not self.collid(self.y_pos-1, self.x_pos):
            self.y_pos -= 1
            self.get_coin(self.y_pos, self.x_pos)

    def move_down(self):
        self.rotate('down')
        if not self.collid(self.y_pos+1, self.x_pos):
            self.y_pos += 1
            self.get_coin(self.y_pos, self.x_pos)

    def move_left(self):
        self.rotate('left')
        if not self.collid(self.y_pos, self.x_pos-1):
            self.x_pos -= 1
            self.get_coin(self.y_pos, self.x_pos)

    def move_right(self):
        self.rotate('right')
        if not self.collid(self.y_pos, self.x_pos+1):
            self.x_pos += 1
            self.get_coin(self.y_pos, self.x_pos)

    def rotate(self, direction):
        self.player = pygame.image.load(
            'images/pacman-{}.png'.format(direction))

    def create(self, surface):
        self.checkWin()
        surface.blit(self.player, (self.x_pos*44, self.y_pos*44))

    def checkWin(self):
        if len(coins) == 0:
            self.winner = True

    def collid(self, i, j):
        return self.map.matriz[i][j] == 1

    def get_coin(self, i, j):
        if self.map.matriz[i][j] == 0:
            self.score += 100
            self.song.set_volume(0.05)
            self.song.play()
            self.map.matriz[i][j] = None


class Maze:
    matriz = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, None, None, None, None, 0, None, None,
                  None, None, None, 1, None, None, None, 1],
              [1, 1, 1, 1, 1, 1, None, 1, None, None,
                  0, None, None, 0, None, 1],
              [1, 0, None, 1, 1, 1, None, None,
                  None, 1, None, None, 1, 1, 1, 1],
              [1, None, None, 1, None, None, None, 0,
                  None, 1, None, None, 1, 1, 1, 1],
              [1, None, None, 1, 1, 1, 1, None, None,
                  1, None, None, None, None, None, 1],
              [1, 1, None, None, None, None, None, None,
                  None, 1, None, None, None, None, 0, 1],
              [1, None, 0, None, 1, 1, None, 1, None,
                  None, None, None, None, None, 1, 1],
              [1, None, None, None, 1, 1, 0, None,
                  None, None, None, 1, 1, None, 1, 1],
              [1, None, None, None, 1, 1, None, None,
                  None, None, 0, 1, 1, 0, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def create(self, surface, block_maze, size):
        global coins
        aux_coins = []

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[1])):
                surface.blit(block_maze, (j*size, i*size)) if self.matriz[i][j] == 1 else \
                    aux_coins.append(surface.blit(pygame.image.load('images/fruit.png'), (j*size, i*size))) \
                    if self.matriz[i][j] == 0 else None

        coins = aux_coins
