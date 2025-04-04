import pygame, sys, random
from pygame.locals import *

pygame.init()

FPS = 10
FramePerSec = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SPEED = 10 
SEGMENT_SIZE = 10 

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

UP = (0, -SPEED)
DOWN = (0, SPEED)
LEFT = (-SPEED, 0)
RIGHT = (SPEED, 0)

score = 0
level = 1


font = pygame.font.Font(None, 30)

class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)] # создание 3 сегментов
        self.direction = RIGHT

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1]) # создание новой головы

        if new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT:
            game_over()

        self.body.insert(0, new_head)

        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction: # проверка что бы змейка не могла поменять направление внутрь себя
            self.direction = new_direction

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, BLACK, (segment[0], segment[1], SEGMENT_SIZE, SEGMENT_SIZE))

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SEGMENT_SIZE, SEGMENT_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.spawn()
        
    def spawn(self):
        self.rect.topleft = (
            random.randint(0, (SCREEN_WIDTH - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE,
            random.randint(0, (SCREEN_HEIGHT - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE,
        )
        self.start_time = pygame.time.get_ticks()  # сохранение времени появления

    def is_expired(self):
        elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
        return elapsed_time > 5

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)


def game_over():
    print("Game Over!")
    pygame.quit()
    sys.exit()

snake = Snake()
apple = Apple()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(RIGHT)

    snake.move()
    if apple.is_expired():
        apple.kill()
        apple.spawn()
    if snake.body[0] == apple.rect.topleft: # проверка если змейка съела яблоко
        
        apple.spawn()
        a = random.randint(1,3)
        score += a
        for i in range(a):
            snake.grow()

        if score % 5 == 0:
            level += 1
            FPS += 2

    DISPLAYSURF.fill(WHITE)
    
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(level_text, (10, 30))

    snake.draw(DISPLAYSURF)
    apple.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)
