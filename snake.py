import sys
import random
import pygame





WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20


assert WINDOW_WIDTH % CELL_SIZE == 0, "WINDOW_WIDTH must be a multiple of CELL_SIZE"
assert WINDOW_HEIGHT % CELL_SIZE == 0, "WINDOW_HEIGHT must be a multiple of CELL_SIZE"

CELL_WIDTH = WINDOW_WIDTH // CELL_SIZE
CELL_HEIGHT = WINDOW_HEIGHT // CELL_SIZE


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
import sys
import random
import pygame

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20

assert WINDOW_WIDTH % CELL_SIZE == 0, "WINDOW_WIDTH must be a multiple of CELL_SIZE"
assert WINDOW_HEIGHT % CELL_SIZE == 0, "WINDOW_HEIGHT must be a multiple of CELL_SIZE"

CELL_WIDTH = WINDOW_WIDTH // CELL_SIZE
CELL_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 120, 0)
GRAY = (40, 40, 40)


def draw_text(surface, text, size, color, x, y, center=False):
    font = pygame.font.SysFont(None, size)
    s = font.render(text, True, color)
    rect = s.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surface.blit(s, rect)


def get_random_location(snake):
    while True:
        x = random.randint(0, CELL_WIDTH - 1)
        y = random.randint(0, CELL_HEIGHT - 1)
        if (x, y) not in snake:
            return (x, y)


def draw_cell(surface, position, color):
    x, y = position
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, color, rect)


def show_game_over(surface, score):
    surface.fill(BLACK)
    draw_text(surface, "Игра окончена", 64, RED, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50, center=True)
    draw_text(surface, f"Счёт: {score}", 36, WHITE, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 10, center=True)
    draw_text(surface, "Нажмите R чтобы начать заново, Esc чтобы выйти", 24, GRAY, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60, center=True)
    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Змейка")
    clock = pygame.time.Clock()

    speed = 10
    move_delay = 1000 // speed
    last_move = pygame.time.get_ticks()

    start_x = CELL_WIDTH // 2
    start_y = CELL_HEIGHT // 2
    snake = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
    direction = (1, 0)

    apple = get_random_location(snake)
    score = 0
    running = True
    game_over = False

    while running:
        now = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if not game_over:
                    if event.key == pygame.K_UP and direction != (0, 1):
                        direction = (0, -1)
                    elif event.key == pygame.K_DOWN and direction != (0, -1):
                        direction = (0, 1)
                    elif event.key == pygame.K_LEFT and direction != (1, 0):
                        direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                        direction = (1, 0)
                else:
                    if event.key == pygame.K_r:
                        snake = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
                        direction = (1, 0)
                        apple = get_random_location(snake)
                        score = 0
                        game_over = False
                        last_move = pygame.time.get_ticks()

        if not game_over and now - last_move >= move_delay:
            last_move = now
            head_x, head_y = snake[0]
            dx, dy = direction
            new_head = (head_x + dx, head_y + dy)

            if (new_head[0] < 0 or new_head[0] >= CELL_WIDTH or
                    new_head[1] < 0 or new_head[1] >= CELL_HEIGHT):
                game_over = True
            else:
                if new_head in snake:
                    game_over = True
                else:
                    snake.insert(0, new_head)
                    if new_head == apple:
                        score += 1
                        if score % 5 == 0:
                            speed += 1
                            move_delay = 1000 // speed
                        apple = get_random_location(snake)
                    else:
                        snake.pop()

        screen.fill(BLACK)

        for x in range(0, WINDOW_WIDTH, CELL_SIZE):
            pygame.draw.line(screen, (20, 20, 20), (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
            pygame.draw.line(screen, (20, 20, 20), (0, y), (WINDOW_WIDTH, y))

        draw_cell(screen, apple, RED)

        for i, pos in enumerate(snake):
            color = DARK_GREEN if i == 0 else GREEN
            draw_cell(screen, pos, color)

        draw_text(screen, f"Счёт: {score}", 24, WHITE, 10, 10)

        if game_over:
            show_game_over(screen, score)
        else:
            pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
