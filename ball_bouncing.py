# pygame import
import pygame

# pygame display initialization
pygame.init()
display = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
FPS = 60

ACCELERATION = .5

class Ball:
    def __init__(self):
        self.position = 100
        self.velocity = 10

    def draw(self):
        pygame.draw.circle(display, (255, 0, 0), (640, self.position), 10, width=20)

    def move(self):
        self.velocity += ACCELERATION
        self.position += self.velocity

        if self.position >= 340:
            self.velocity = -self.velocity


def game():
    ball = Ball() # instance of ball
    while running:
        for event in pygame.event.get(): # cycles through events in game
            if event.type == pygame.QUIT: # if red X then game will close
                return
        ball.move() # move ball

        # draw ball
        display.fill((255, 255, 255)) # bg color for display
        pygame.draw.line(display, (0, 0, 0), (0, 360), (1280, 360), 10 )
        ball.draw()

        # update screen
        pygame.display.update()
        clock.tick(FPS)

game()
pygame.quit()



