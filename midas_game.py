import pygame
import random
pygame.init()

# Pygame Setup
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Midas Touch")

FPS = 20
Clock = pygame.time.Clock()

# Midas Player
midas_SIZE = 50
SQUARE_SIZE = 50
midas_x = WINDOW_WIDTH//2
midas_y = WINDOW_HEIGHT//2
midas_speed = 50

square_x = random.randint(0, WINDOW_WIDTH - SQUARE_SIZE)
square_y = random.randint(0, WINDOW_HEIGHT - SQUARE_SIZE)
square_color = (0, 0,255)
square_color1 = (0, 0, 255)
square_color2 = (0, 0, 255)
square_color3 = (0, 0, 255)

gameloop = True
while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    midas_x = midas_x - 10
                if event.key == pygame.K_RIGHT:
                    midas_x = midas_x + 10
                if event.key == pygame.K_UP:
                    midas_y = midas_y - 10
                if event.key == pygame.K_DOWN:
                    midas_y = midas_y + 10

        midas_rect = pygame.draw.rect(display_surface, "red", (midas_x, midas_y, midas_SIZE, midas_SIZE))
        square_rect1 = pygame.draw.rect(display_surface, "blue", (50, 40, SQUARE_SIZE, SQUARE_SIZE))
        square_rect2 = pygame.draw.rect(display_surface, "blue", (500, 40, SQUARE_SIZE, SQUARE_SIZE))
        square_rect3 = pygame.draw.rect(display_surface, "blue", (50, 500, SQUARE_SIZE, SQUARE_SIZE))
        square_rect4 = pygame.draw.rect(display_surface, "blue", (500, 510, SQUARE_SIZE, SQUARE_SIZE))

        if midas_rect.colliderect(square_rect1):
             square_color = (255, 215, 0)
        if midas_rect.colliderect(square_rect2):
             square_color1 = (255, 215, 0)
        if midas_rect.colliderect(square_rect3):
             square_color2 = (255, 215, 0)
        if midas_rect.colliderect(square_rect4):
             square_color3 = (255, 215, 0)

    display_surface.fill((255, 255, 255))
    pygame.draw.rect(display_surface, (255, 0, 0), midas_rect)
    pygame.draw.rect(display_surface, square_color, square_rect1)
    pygame.draw.rect(display_surface, square_color1, square_rect2)
    pygame.draw.rect(display_surface, square_color2, square_rect3)
    pygame.draw.rect(display_surface, square_color3, square_rect4)

    pygame.display.flip()
    Clock.tick(FPS)

pygame.quit()
