from conf import *
from pacman import *
import os


class Game:
    def __init__(self):
        self.exit_game = False
        self.context = None
        self.frame = None
        self.blocks = None
        self.pacman = Pacman()
        print("Escolha a dificuldade do jogo \n 1- Para Fácil \n 2- Para Médio \n 3- Para Difícil")
        self.map = Maze(int(input())-1)
        self.game_over = None
        self.score = None
        self.time = None

    def init(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption("SIMPLE PAC MAN INVERTED")
        self.score = pygame.font.Font(None, 20)
        self.time = pygame.font.Font(None, 20)
        self.context = pygame.display.set_mode((HEIGHT, WIDTH))
        self.blocks = pygame.image.load("images/block_maze.png").convert()
        self.blocks = pygame.transform.scale(self.blocks, (45, 45))
        self.frame = pygame.time.Clock()
        self.exit_game = False
        self.game_over = pygame.font.Font(None, 80).render("GAME OVER", 0, RED)

    def create(self, time):
        self.context.fill(BLACK)
        self.map.create(self.context, self.blocks, 44)
        self.pacman.create(self.context, YELLOW)
        self.context.blit(self.score.render(f'Score:{self.pacman.score}', 0, WHITE), (HEIGHT-80, 10))
        self.context.blit(self.time.render(f'Time:{time}', 0, WHITE), (HEIGHT-80, 30))
        self.frame.tick(15)
        pygame.display.update()

    def quit_event(self, event):
        for evt in event:
            if evt.type == pygame.QUIT:
                self.exit_game = True

    def animation(self, key):
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
        total_time = 25
        pygame.mixer.music.load('sounds/game.ogg')
        pygame.mixer.music.play(2, 8)

        while not self.exit_game:
            time = pygame.time.get_ticks()//1000
            self.quit_event(pygame.event.get())
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            self.animation(keys)

            if total_time - time == 0:
                self.context.fill(WHITE)
                self.context.blit(self.game_over, (HEIGHT/2-150, WIDTH/2-30))
                pygame.display.update()
                pygame.time.delay(3000)
                self.exit_game = True
            else:
                self.create(total_time-time)

            if self.pacman.winner:
                    win = pygame.font.Font(None, 80).render("YOU WIN", 0, GREEN)
                    self.context.fill(WHITE)
                    self.context.blit(win, (HEIGHT/2-150, WIDTH/2-30))
                    pygame.display.update()
                    pygame.time.delay(5000)
                    self.exit_game = True



