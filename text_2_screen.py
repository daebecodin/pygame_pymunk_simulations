import pygame

pygame.init()
display = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
FPS = 60

def print_text(text, position, size):
    font = pygame.font.SysFont("Poppins", size, True, False)
    surface = font.render(text, True, (255, 153, 153))
    display.blit(surface, position)

def game():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill((153, 204, 255))
        print_text("dummy text 1", (100,100), 40)
        print_text("dummy text 2", (500,500), 60)
        pygame.display.update()
        clock.tick(FPS)

game()
pygame.quit()