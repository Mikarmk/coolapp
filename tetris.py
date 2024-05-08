import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пиксельная стрелялка с постоянными атаками врагов")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT - 50
        self.lives = 3
        self.score = 0

    def move_left(self):
        self.rect.x -= 5

    def move_right(self):
        self.rect.x += 5

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullet_group.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed_y = random.randint(1, 5)
        self.shoot_timer = 0

    def update(self):
        self.rect.y += self.speed_y
        self.shoot_timer += 1
        if self.shoot_timer >= 30:
            self.shoot_timer = 0
            bullet = EnemyBullet(self.rect.centerx, self.rect.bottom)
            all_sprites.add(bullet)
            enemy_bullet_group.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width // 2
        self.rect.y = y

    def update(self):
        self.rect.y += 5
        if self.rect.top > HEIGHT:
            self.kill()

class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed_y = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT:
            self.kill()

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
bonus_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)
player_group.add(player)

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

    if len(enemy_group) < 10 and random.randint(0, 100) < 2:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemy_group.add(enemy)
    if len(bonus_group) < 3 and random.randint(0, 100) < 1:
        bonus = Bonus()
        all_sprites.add(bonus)
        bonus_group.add(bonus)

    all_sprites.update()

    hits = pygame.sprite.groupcollide(bullet_group, enemy_group, True, True)
    for hit in hits:
        player.score += 10
    hits = pygame.sprite.spritecollide(player, enemy_bullet_group, True)
    for hit in hits:
        player.lives -= 1
    hits = pygame.sprite.spritecollide(player, bonus_group, True)
    for hit in hits:
        if random.randint(0, 1) == 0:
            player.lives += 1
        else:
            player.score += 50

    screen.fill(BLACK)
    all_sprites.draw(screen)
    font = pygame.font.Font(None, 36)
    text = font.render(f"Счет: {player.score}", True, WHITE)
    screen.blit(text, (10, 10))
    text = font.render(f"Жизни: {player.lives}", True, WHITE)
    screen.blit(text, (10, 40))
    pygame.display.flip()

pygame.quit()
