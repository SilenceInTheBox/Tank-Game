from utilities import *
# from pygame.locals import *


# canvas init
pygame.init()
pygame.display.set_caption("End of Game Example")

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

RUNNING = True
END = False
height = screen.get_height()
width = screen.get_width()
num_balls = 1


# object init
player = Player(width/2, height/2)
balls = [Ball(width*r.random()) for _ in range(num_balls)]

objects = [player] + balls


# logic loop
while RUNNING:
    for event in pygame.event.get():

        print(event, event.type)
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == CUSTOM_EVENT_TYPE:
            print("END")
            END = True
            break
    if END:
        break

    screen.fill((171, 101, 164))
    dt = clock.tick(60) / 100

    for i in objects:
        i.update(dt, screen)

    check_for_collisions(player, balls)

    pygame.display.flip()


button_x = width/2
button_y = height*2/3
button_width = 50
button_height = 20
button_stats = (button_x, button_y, button_width, button_height)

while END:
    for event in pygame.event.get():
        if event.type == pygame.K_RETURN:
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            print(check_mouse_pos(event.pos, button_stats))
        if (event.type == pygame.MOUSEBUTTONDOWN and check_mouse_pos(event.pos, button_stats)):
            END = False
    message = font.render("End of Game!", True, 'white')
    screen.blit(message, (width/2-button_width/2, height/2))

    exit_button = pygame.draw.rect(
        screen, "red", (width/2-button_width/2, height*2/3-button_height/2, button_width, button_height))
    exit_text = font.render("Exit", True, 'black')
    screen.blit(exit_text, (width/2-button_width /
                2, height*2/3-button_height/2))
    pygame.display.flip()


pygame.quit()
