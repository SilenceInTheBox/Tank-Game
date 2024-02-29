import pygame
import random as r


CUSTOM_EVENT_TYPE = pygame.USEREVENT + 1
custom_event = pygame.event.Event(CUSTOM_EVENT_TYPE, message='custom event!')


def check_for_collisions(player, objects):

    for o in objects:
        p_pos = player.get_pos()
        o_pos = o.get_pos()
        rel_pos = p_pos - o_pos
        dist = rel_pos.length()

        if dist < (player.radius + o.radius):
            pygame.event.post(custom_event)


def check_mouse_pos(pos0, button_stats):
    bx, by, width, height = button_stats
    if bx - width/2 < pos0[0] and pos0[0] < bx + width/2 and \
            by - height/2 < pos0[1] and pos0[1] < by + height/2:
        return True
    else:
        return False


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

        pygame.draw.circle(screen, (39, 99, 90), self.get_pos(), self.radius)


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
            if r.random() > 0.9:
                self.alive = True
                self.x = r.random() * screen.get_width()


if __name__ == '__main__':
    button_stats = (100, 100, 50, 50)
    pos0 = (90, 100)

    print(check_mouse_pos(pos0, button_stats))
