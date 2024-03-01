import pygame
from scipy import interpolate
import random as r
from math import sin, cos


def check_game_end(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def winning_message(screen, winning_player):
    screen.fill((66, 135, 85))
    font = pygame.font.Font(None, 36)
    win_mes = font.render(
        f'Congratulations {winning_player.name}! You won!', True, "white")
    screen.blit(win_mes, (screen.get_width()//3, screen.get_height()//2))
    pygame.display.flip()
    while True:
        events = pygame.event.get()
        check_game_end(events)


class Ground:
    def __init__(self, width, height) -> None:
        self.xs, self.ys = self.get_random_coords(width, height)

    def get_coords(self):
        return list(zip(self.xs, self.ys))

    def get_random_coords(self, width, height, n=101, num_supp=9):
        xs = [i*width/(n-1) for i in range(n)]
        xsupp = [i*width/(num_supp-1) for i in range(num_supp)]
        ysupp = [0.5*height*r.random() for x in xsupp]
        CubInt = interpolate.CubicSpline(xsupp, ysupp)
        ys = CubInt(xs)
        ys = [height - 10 - (i-min(ys)) for i in ys]
        return xs, ys

    def draw(self, screen):
        pygame.draw.lines(screen, 'white', closed=False,
                          points=self.get_coords())


class Player:
    def __init__(self, name, x, y) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.alive = True
        self.aim = 0
        self.power = 0

    def get_pos(self):
        return pygame.Vector2(self.x, self.y)

    def get_aim(self):
        return pygame.Vector2(sin(self.aim), -cos(self.aim))

    def get_shot_vec(self):
        aim_vec = self.get_aim()
        return aim_vec * self.power

    def draw(self, screen):
        pygame.draw.rect(screen, "red", (self.x-5, self.y-10, 10, 10))

    def draw_aim(self, screen):
        arrow = self.get_aim()
        start = (self.x + 50*arrow.x, self.y + 50*arrow.y)
        end = (self.x + 100*arrow.x, self.y + 100*arrow.y)
        pygame.draw.line(screen, 'red', start, end, width=2)


class Bullet:
    def __init__(self, pos, vel) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.vx = vel[0]
        self.vy = vel[1]
        self.ay = 5

        self.STATUS = None

    def get_pos(self):
        return pygame.Vector2(self.x, self.y)

    def draw(self, screen):
        pygame.draw.circle(screen, 'blue', self.get_pos(), 1)

    def update_pos(self, dt):
        self.vy += self.ay * dt
        self.y += self.vy * dt
        self.x += self.vx * dt

    def check_ground_collision(self, ground):
        ground_coords = ground.get_coords()
        for (x0, y0), (x1, y1) in zip(ground_coords, ground_coords[1:]):
            if x0 <= self.x <= x1:
                if self.y > (y0 + y1)/2:
                    return True
                else:
                    return False

    def check_enemy_hit(self, enemy):
        enmy_pos = enemy.get_pos()
        own_pos = self.get_pos()
        dist = (enmy_pos - own_pos).length()
        if dist < 50:
            return True
        else:
            return False

    def check_out_of_bounds(self, screen):
        x, y = self.get_pos()
        width = screen.get_width()
        height = screen.get_height()
        if x < 0 or width < x or y < 0 or height < y:
            return True
        else:
            return False

    def simulate(self, screen, dt, ground, enemy):
        j = 0
        while True:
            j += 1
            self.update_pos(dt)
            self.draw(screen)
            if self.check_ground_collision(ground) and j > 150:
                print('Shot collided with terrain.')
                self.STATUS = 'GRD'
                break
            if self.check_enemy_hit(enemy):
                print('Hit! Enemy destroyed.')
                self.STATUS = 'HIT'
                break
            if self.check_out_of_bounds(screen):
                print('Shot out of bounds...')
                self.STATUS = 'OOB'
                break
            pygame.display.flip()


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    b = Bullet((10, 10), (3, 3))
