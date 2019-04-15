import pygame

level = 0
score = 18
coins = []


class Pacman:
    global level
    global coins
    x_pos, y_pos, = 1, 1
    player = None

    def __init__(self):
        self.map = Maze()
        self.score = 0
        self.winner = False
        pygame.mixer.init()
        self.song = pygame.mixer.Sound('sounds/eat.wav')

    def move_up(self):
        if not self.collid(self.y_pos-1, self.x_pos):
            self.y_pos -= 1
            self.get_coin(self.y_pos, self.x_pos)

    def move_down(self):
        if not self.collid(self.y_pos+1, self.x_pos):
            self.y_pos += 1
            self.get_coin(self.y_pos, self.x_pos)

    def move_left(self):
        if not self.collid(self.y_pos, self.x_pos-1):
            self.x_pos -= 1
            self.get_coin(self.y_pos, self.x_pos)

    def move_right(self):
        if not self.collid(self.y_pos, self.x_pos+1):
            self.x_pos += 1
            self.get_coin(self.y_pos, self.x_pos)

    def create(self, surface, color):
        #self.player = (pygame.draw.ellipse(surface, color, (self.x_pos*44, self.y_pos*44, 30, 30)))
        self.player = pygame.image.load('images/ghost.png')
        surface.blit(self.player, (self.x_pos*44, self.y_pos*44))

    def collid(self, i, j):
        return self.map.levels[level][i][j] == 1

    def get_coin(self, i, j):

        if self.map.levels[level][i][j] == 0:
            self.score += 100
            self.song.set_volume(0.05)
            self.song.play()
            self.map.levels[level][i][j] = None
        if len(coins) == 0:
            self.winner = True


class Maze:
    matriz = [[1,1,1,1,1,1,1,1,1,1],
             [1,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,1,1,0,0,0,1],
             [1,0,1,1,1,1,0,0,0,1],
             [1,0,1,0,0,0,0,0,0,1],
             [1,0,1,1,1,1,1,0,0,1],
             [1,0,0,0,0,0,0,0,0,1],
             [1,1,1,1,1,1,1,1,1,1]]

    matriz2 = [[1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,1,0,0,0,0,0,0,0,0,1,1],
                [1,0,1,0,1,1,0,1,0,0,0,0,1],
                [1,0,1,1,1,1,0,0,0,1,0,0,1],
                [1,0,1,0,0,0,0,0,0,1,0,0,1],
                [1,0,1,1,1,1,1,0,0,1,0,0,1],
                [1,0,0,0,0,0,0,0,0,1,0,0,1],
                [1,0,0,1,1,1,0,0,0,0,0,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1]]

    matriz3 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1],
                [1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,0,0,0,1,0,0,1,1,1,1],
                [1,0,1,0,0,0,0,0,0,1,0,0,1,0,1,1],
                [1,0,1,1,1,1,1,0,0,1,0,0,0,0,0,1],
                [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
                [1,0,0,1,1,1,0,1,0,0,0,0,0,0,1,1],
                [1,0,0,1,1,1,0,0,0,0,0,1,1,0,1,1],
                [1,0,0,1,1,1,0,0,0,0,0,1,1,0,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

    levels = (matriz, matriz2, matriz3)

    def __init__(self, nvl=1):
        self.level = nvl

    def create(self, surface, block_maze, size):
        global level
        global coins
        level = self.level
        aux_coins = []
        for i in range(len(self.levels[level])):
            for j in range(len(self.levels[level][1])):
                surface.blit(block_maze, (j*size, i*size)) if self.levels[level][i][j] == 1 else \
                      aux_coins.append(surface.blit(pygame.image.load('images/coin.png'), (j*size, i*size))) \
                      if self.levels[level][i][j] == 0 else None

        coins = aux_coins
