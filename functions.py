import pygame
from scipy import interpolate
import random as r
from math import sin, cos


def check_game_end(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


class Ground:
    def __init__(self, width, height) -> None:
        self.xs, self.ys = self.get_random_coords(width, height)

    def get_coords(self):
        return list(zip(self.xs, self.ys))

    def get_random_coords(self, width, height, n=500):
        xs = [i*width/(n-1) for i in range(n)]
        xsupp = xs[::n//9]
        ysupp = [0.5*height*r.random() for x in xsupp]
        CubInt = interpolate.CubicSpline(xsupp, ysupp)
        ys = CubInt(xs)
        xs = [i for i in xs]
        ys = [height - 0.8*height*i/max(abs(ys)) for i in ys]
        return xs, ys

    def draw(self, screen):
        pygame.draw.lines(screen, 'white', closed=False,
                          points=self.get_coords())


class Player:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.alive = True
        self.aim = 0
        self.power = 0

    def get_pos(self):
        return pygame.Vector2(self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, "red", (self.x-5, self.y-10, 10, 10))

    def draw_aim(self, screen):
        arrow = pygame.Vector2(sin(self.aim), -cos(self.aim))
        start = (self.x + 50*arrow.x, self.y + 50*arrow.y)
        end = (self.x + 100*arrow.x, self.y + 100*arrow.y)
        pygame.draw.line(screen, 'red', start, end, width=2)


class Bullet:
    def __init__(self, pos, vel) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.vx = vel[0]
        self.vy = vel[1]
        self.ay = -5

    def get_pos(self):
        return pygame.Vector2(self.x, self.y)


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    p1 = Player(100, 100)
    None
