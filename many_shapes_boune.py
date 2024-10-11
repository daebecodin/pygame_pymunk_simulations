import pygame

pygame.init()
WIDTH, HEIGHT = 1280, 720
widthHalf = WIDTH / 2
heightHalf = HEIGHT / 2

display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
FPS = 60

ACCELERATION = .5

class Shape:
    def __init__(self):
        self.position = HEIGHT / 7
        self.velocity = 10

    def move(self):
        self.velocity += ACCELERATION
        self.position += self.velocity

        if self.position >= (HEIGHT / 2) - 20:
            self.velocity = -self.velocity

class Square(Shape):
    def draw(self):
        pygame.draw.rect(display, (250, 117, 132), [WIDTH / 7, self.position, 50,50], )

    def move(self):
        self.velocity += ACCELERATION
        self.position += self.velocity
        if self.position >= 340 - 50:
            self.velocity = -self.velocity

class Ball(Shape):
    def draw(self):
        pygame.draw.circle(display,(250, 168, 117), (WIDTH / 2, self.position), 10, width = 20 )

class Triangle(Shape):
    def draw(self):
        pygame.draw.polygon(display, (117, 250, 138), [[WIDTH / 1.2, self.position], [WIDTH / 1.11, self.position], [WIDTH / 1.15, self.position - 50]])


def game():
    square = Square()
    ball = Ball()
    triangle = Triangle()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        square.move()
        ball.move()
        triangle.move()


        display.fill((117, 193, 250))
        pygame.draw.line(display, (0, 0, 0), (0, heightHalf), (WIDTH, heightHalf), 10 )

        square.draw()
        ball.draw()
        triangle.draw()

        pygame.display.update()
        clock.tick(FPS)

game()
pygame.quit()