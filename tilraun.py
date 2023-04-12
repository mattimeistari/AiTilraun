import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 144
fpsClock = pygame.time.Clock()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Verkefni 028")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BROWN = (189, 154, 122)
GREEN = (0, 110, 51)
BLUE = (0, 138, 216)
PINK = (255, 193, 204)
YELLOW = (255, 255, 153)
BLACK = (0, 0, 0)

rect_x = 200
rect_y = 200
speed = 10
screen.fill(WHITE)
fart=False

currentColor = BROWN

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        if fart == True:
                rect_y = 200
                rect_x = 200
                screen.fill(WHITE)
                fart=False

        elif event.type == pygame.KEYDOWN:
            prev_x = rect_x
            prev_y = rect_y

        # Movement
            if event.key == pygame.K_w:
                moving_up = True
            elif event.key == pygame.K_s:
                moving_down = True
            elif event.key == pygame.K_a:
                moving_left = True
            elif event.key == pygame.K_d:
                moving_right = True

        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    moving_up = False
                elif event.key == pygame.K_s:
                    moving_down = False
                elif event.key == pygame.K_a:
                    moving_left = False
                elif event.key == pygame.K_d:
                    moving_right = False

        if moving_up:
            rect_y -= speed
        elif moving_down:
            rect_y += speed
        if moving_left:
            rect_x -= speed
        elif moving_right:
            rect_x += speed

        if rect_x < 0 or rect_x + 10 > screen_width or rect_y < 0 or rect_y + 10 > screen_height:
                rect_x = prev_x
                rect_y = prev_y

        # Colors
         elif event.type == pygame.KEYDOWN:
            elif event.key == pygame.K_r:
                currentColor = RED
            elif event.key == pygame.K_y:
                currentColor = YELLOW
            elif event.key == pygame.K_j:
                currentColor = BLACK
            elif event.key == pygame.K_g:
                currentColor = GREEN
            elif event.key == pygame.K_b:
                currentColor = BLUE
            elif event.key == pygame.K_p:
                currentColor = PINK
            elif event.key == pygame.K_e:
                currentColor = WHITE

        # Reset
            elif event.key == pygame.K_n:
                rect_y = 200
                rect_x = 200
                screen.fill(WHITE)
                fart=True

            prevColor = screen.get_at((rect_x, rect_y))
            pygame.draw.rect(screen, prevColor, (prev_x, prev_y, 10, 10))
            pygame.draw.rect(screen, RED, (rect_x, rect_y, 10, 10), 1)

    
    pygame.draw.rect(screen, RED, (rect_x, rect_y, 10, 10), 1)
    pygame.display.flip()
    fpsClock.tick(144)

pygame.quit()
