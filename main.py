from utilities import *

pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True

height = screen.get_height()
width = screen.get_width()


player = Player(width/2, height/2)
ball = Ball(width*r.random())


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('purple')
    dt = clock.tick(60) / 100

    player.update(dt, screen)
    ball.update(dt, screen)

    pygame.display.flip()


pygame.quit()
