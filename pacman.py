import pygame


class Pacman:
    x_pos, y_pos, speed = 50, 50, 5
    player = None

    def move_up(self):
        self.y_pos = self.y_pos - self.speed

    def move_down(self):
        self.y_pos = self.y_pos + self.speed

    def move_left(self):
        self.x_pos = self.x_pos - self.speed

    def move_right(self):
        self.x_pos = self.x_pos + self.speed

    def create(self, surface, color):
        self.player = (pygame.draw.ellipse(surface, color, (self.x_pos, self.y_pos, 30, 30)))


class Map:
    def __init__(self):
        self.map_height = 10
        self.map_width = 8
        self.map_easy = [1,1,1,1,1,1,1,1,1,1,
                         1,0,0,0,1,0,0,0,1,1,
                         1,0,0,0,0,0,0,0,0,1,
                         1,0,1,1,1,1,1,1,0,1,
                         1,0,1,0,0,0,0,0,0,1,
                         1,0,1,0,1,1,1,1,0,1,
                         1,0,0,0,0,0,0,0,0,1,
                         1,1,1,1,1,1,1,1,1,1]

    def create(self, surface, block_maze):
        x0, y0 = 0, 0
        for i in range(0, self.map_height * self.map_width):
            if self.map_easy[x0 + (y0*self.map_height)] == 1:
                surface.blit(block_maze, (x0 * 44, y0 * 44))

            x0 += 1
            if x0 > self.map_height-1:
                x0 = 0
                y0 += 1

