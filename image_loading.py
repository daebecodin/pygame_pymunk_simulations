import pygame

pygame.init()
WIDTH, HEIGHT = 1280, 720
widthHalf = WIDTH / 2
heightHalf = HEIGHT / 2

display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
FPS = 60

def game():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    display.fill((117, 193, 250))

    pygame.display.update()
    clock.tick(FPS)

game()
pygame.quit()