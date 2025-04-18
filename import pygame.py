import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shadow Dodge")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT = (255, 255, 102)
NINJA_COLOR = (50, 50, 50)

font = pygame.font.SysFont("comicsansms", 30)

clock = pygame.time.Clock()

ninja_size = 40
ninja_x = WIDTH // 2
ninja_y = HEIGHT - ninja_size - 10
ninja_speed 

beams = []
beam_width = 80
beam_height = 20
beam_speed = 5
beam_timer = 0

score = 0
start_time = pygame.time.get_ticks()


def draw_ninja(x, y):
    pygame.draw.rect(screen, NINJA_COLOR, (x, y, ninja_size, ninja_size))


def draw_beams(beams):
    for beam in beams:
        pygame.draw.rect(screen, LIGHT, beam)


def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))


def game_over_screen(score):
    screen.fill(BLACK)
    text = font.render(f"Game Over! Score: {score}", True, WHITE)
    screen.blit(text, (WIDTH // 6, HEIGHT // 2 - 20))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()


def game_loop():
    global ninja_x, beams, beam_timer, beam_speed

    run = True
    while run:
        clock.tick(60)
        screen.fill(B)
        score = (pygame.time.get_ticks() - start_time) // 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ninja_x > 0:
            ninja_x -= ninja_speed
        if keys[pygame.K_RIGHT] and ninja_x < WIDTH - ninja_size:
            ninja_x += ninja_speed

        beam_timer += 1
        if beam_timer >= 30:
            beam_x = random.randint(0, WIDTH - beam_width)
            beams.append(pygame.Rect(beam_x, -beam_height, beam_width, beam_height))
            beam_timer = 0

        for beam in beams:
            beam.y += beam_speed

        beams = [b for b in beams if b.y < HEIGHT]

        ninja_rect = pygame.Rect(ninja_x, ninja_y, ninja_size, ninja_size)
        for beam in beams:
            if ninja_rect.colliderect(beam):
                game_over_screen(score)

        if score % 10 == 0 and score != 0:
            beam_speed = 5 + score // 10

        draw_ninja(ninja_x, ninja_y)
        draw_beams(beams)
        show_score(score)
        pygame.display.update()

    pygame.quit()


game_loop()
