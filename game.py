from conf import *
from pacman import *


class Game:
    def __init__(self):
        self.exit_game = False
        self.context = None
        self.frame = None
        self.blocks = None
        self.pacman = Pacman()
        self.map = Map()
        self.place = []

    def init(self):
        pygame.init()
        pygame.display.set_caption("SIMPLE PAC MAN")
        self.context = pygame.display.set_mode((HEIGHT, WIDTH))
        self.blocks = pygame.image.load("images/block_maze.png").convert()
        self.blocks = pygame.transform.scale(self.blocks, (45, 45))
        self.map.create(self.context, self.blocks)
        self.frame = pygame.time.Clock()
        self.exit_game = False

    def create(self):
        self.context.fill(BLACK)
        self.pacman.create(self.context, YELLOW)
        self.map.create(self.context, self.blocks)
        self.frame.tick(15)

        pygame.display.update()

    def quit_event(self, event):
        for evt in event:
            if evt.type == pygame.QUIT:
                self.exit_game = True

    def animation(self, key):
        y_before, x_before = self.pacman.y_pos, self.pacman.x_pos
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.pacman.move_left()

        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.pacman.move_right()

        if key[pygame.K_UP] or key[pygame.K_w]:
            self.pacman.move_up()

        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.pacman.move_down()


    def execute(self):
        self.init()

        while not self.exit_game:
            self.quit_event(pygame.event.get())
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            self.animation(keys)
            self.create()

