import pygame, sys, random, psycopg2
from pygame.locals import *

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
SPEED = 10
SEGMENT_SIZE = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

UP = (0, -SPEED)
DOWN = (0, SPEED)
LEFT = (-SPEED, 0)
RIGHT = (SPEED, 0)

font = pygame.font.Font(None, 30)
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
FramePerSec = pygame.time.Clock()

def get_connection():
    return psycopg2.connect("dbname=postgres user=postgres password=123 host=localhost")

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS snake_users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            score INT DEFAULT 0,
            level INT DEFAULT 1,
            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def get_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, level, score FROM snake_users WHERE username = %s;", (username,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

def create_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO snake_users (username) VALUES (%s) RETURNING id, level, score;", (username,))
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return result

def save_user_progress(user_id, score, level):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE snake_users
        SET score = %s, level = %s, saved_at = CURRENT_TIMESTAMP
        WHERE id = %s;
    """, (score, level, user_id))
    conn.commit()
    cur.close()
    conn.close()

class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = RIGHT

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        if new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT:
            game_over()
        if new_head in self.body:
            game_over()
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
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
            random.randint(0, (SCREEN_HEIGHT - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE
        )
        self.start_time = pygame.time.get_ticks()

    def is_expired(self):
        return (pygame.time.get_ticks() - self.start_time) / 1000 > 5

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

create_table()
username = input("Введите имя пользователя: ")
user_data = get_user(username)

if user_data:
    user_id, level, score = user_data
    print(f"Добро пожаловать, {username}! Уровень: {level}, Счёт: {score}")
else:
    user_id, level, score = create_user(username)
    print(f"Создан новый пользователь: {username}")

FPS = 10 + (level - 1) * 2
paused = False
snake = Snake()
apple = Apple()

def game_over():
    print("Game Over!")
    save_user_progress(user_id, score, level)
    pygame.quit()
    sys.exit()

def pause_game():
    global paused
    paused = not paused
    if paused:
        print("Пауза. Прогресс сохранён.")
        save_user_progress(user_id, score, level)
    else:
        print("Продолжаем игру.")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            save_user_progress(user_id, score, level)
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                snake.change_direction(UP)
            elif event.key == K_DOWN:
                snake.change_direction(DOWN)
            elif event.key == K_LEFT:
                snake.change_direction(LEFT)
            elif event.key == K_RIGHT:
                snake.change_direction(RIGHT)
            elif event.key == K_p:
                pause_game()

    if not paused:
        snake.move()
        if apple.is_expired():
            apple.spawn()
        if snake.body[0] == apple.rect.topleft:
            apple.spawn()
            a = random.randint(1, 3)
            score += a
            for _ in range(a):
                snake.grow()
            if score % 5 == 0:
                level += 1
                FPS += 2

        DISPLAYSURF.fill(WHITE)
        snake.draw(DISPLAYSURF)
        apple.draw(DISPLAYSURF)

        score_text = font.render(f"Score: {score}", True, BLACK)
        level_text = font.render(f"Level: {level}", True, BLACK)
        DISPLAYSURF.blit(score_text, (10, 10))
        DISPLAYSURF.blit(level_text, (10, 30))

        pygame.display.update()
        FramePerSec.tick(FPS)
