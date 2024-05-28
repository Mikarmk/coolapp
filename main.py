import pygame
import random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("AI")

SQUARE_SIZE = 50

LEARNING_RATE = 0.1
REWARD_ABSORB = 1
PENALTY_SPAWN = -0.5

class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.weight = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def absorb(self, other):
        self.weight += other.weight
        return True

    def spawn(self):
        new_x = random.randint(SQUARE_SIZE, WINDOW_WIDTH - SQUARE_SIZE)
        new_y = random.randint(SQUARE_SIZE, WINDOW_HEIGHT - SQUARE_SIZE)
        return Square(new_x, new_y)

square = Square(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
other_squares = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        square.move(5, 0)
    if keys[pygame.K_UP]:
        square.move(0, -5)
    if keys[pygame.K_DOWN]:
        square.move(0, 5)

    for other in other_squares:
        if (square.x - other.x) ** 2 + (square.y - other.y) ** 2 <= (SQUARE_SIZE + 10) ** 2:
            if square.absorb(other):
                other_squares.remove(other)
                square.weight += REWARD_ABSORB

    if random.random() < 0.01:
        new_square = square.spawn()
        other_squares.append(new_square)
        square.weight += PENALTY_SPAWN

    square.weight += LEARNING_RATE * (square.weight - 1)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (square.x, square.y, SQUARE_SIZE, SQUARE_SIZE))
    for other in other_squares:
        pygame.draw.rect(screen, (128, 128, 128), (other.x, other.y, SQUARE_SIZE, SQUARE_SIZE))
    pygame.display.flip()

pygame.quit()
