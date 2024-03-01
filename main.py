import pygame
from functions import *
import time

# A TANK GAME
# -----------
# Inspired by a mini game on my parents PC, I decided trying to implement a similar
# game myself. It should not be too hard with my current skill set.
# I decided to use the pygame library after initial attempt with tkinter did not
# seem to go anywhere.


pygame.init()

width_px = 800
height_px = 600
screen = pygame.display.set_mode((width_px, height_px))
clock = pygame.time.Clock()


RUNNING = True
TURN = 'p1'
PHYSICS_ACTIVE = False

# create terrain
ground = Ground(width_px, height_px)

# spawn players
p1 = Player(ground.xs[100], ground.ys[100])
p2 = Player(ground.xs[500-100], ground.ys[500-100])


while RUNNING:
    check_game_end(pygame.event.get())

    clock.tick(60)
    screen.fill((0, 0, 0))

    ground.draw(screen)
    p1.draw(screen)
    p2.draw(screen)

    active_player = p1 if TURN == 'p1' else p2

    # TURN loop
    while True:
        check_game_end(pygame.event.get())

        clock.tick(60)
        screen.fill((0, 0, 0))

        ground.draw(screen)
        p1.draw(screen)
        p2.draw(screen)

        active_player.draw_aim(screen)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            active_player.aim -= .0005
        if keys[pygame.K_RIGHT]:
            active_player.aim += .0005
        if keys[pygame.K_SPACE]:

            # power measure
            start_time = time.time()
            while True:
                events = pygame.event.get()
                check_game_end(events)
                if pygame.KEYUP in [i.type for i in events] and \
                        pygame.K_SPACE in [i.key for i in events]:
                    end_time = time.time()
                    duration = end_time - start_time
                    active_player.power = duration
                    break

        pygame.display.flip()

    pygame.display.flip()

pygame.quit()
