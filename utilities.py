import pygame
import random as r


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10

    def get_pos(self):
        return pygame.Vector2(self.x, self.y)

    def update(self, dt, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 25 * dt
        if keys[pygame.K_s]:
            self.y += 25 * dt
        if keys[pygame.K_a]:
            self.x -= 25 * dt
        if keys[pygame.K_d]:
            self.x += 25 * dt

        pygame.draw.circle(screen, "black", self.get_pos(), self.radius)


class Ball:
    def __init__(self, x):
        self.x = x
        self.y = 0
        self.yvel = 0
        self.yacc = 3
        self.radius = 15
        self.alive = False

    def get_pos(self):
        return pygame.Vector2(self.x, self.y)

    def update(self, dt, screen):
        if self.alive:
            if self.y > screen.get_height():
                self.alive = False
                self.y = 0
                self.yvel = 0
                self.yacc = 3
                return None
            self.yvel += self.yacc * dt
            self.y += self.yvel * dt
            pygame.draw.circle(screen, "white", self.get_pos(), self.radius)

        else:
            if r.random() > 0.5:
                self.alive = True
                self.x = r.random() * screen.get_width()
