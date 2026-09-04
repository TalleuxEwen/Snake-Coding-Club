#
# /!\ PLEASE DO NOT MODIFY THE CONTENT OF THIS DOCUMENT /!\
#
# This is the entry point of the game.
# It creates the window, listens to keyboard events and calls the
# loop(), draw() and on_key_down() functions defined in game.py
#

import sys

import pygame

import game

WINDOW_TITLE = "A nice little game"
DEFAULT_WINDOW_SIZE = (400, 400)


def show_game_over_overlay(screen):
    font = pygame.font.SysFont(None, 60)
    text = font.render("GAME OVER", True, pygame.Color("red"))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    overlay_rect = text_rect.inflate(40, 40)

    pygame.draw.rect(screen, pygame.Color("black"), overlay_rect)
    pygame.draw.rect(screen, pygame.Color("red"), overlay_rect, 2)
    screen.blit(text, text_rect)


def game_loop():
    pygame.init()
    pygame.display.set_mode(DEFAULT_WINDOW_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()

    # Keep track of elapsed time between frames, similar to a requestAnimationFrame accumulator
    accumulator = 0
    running = True

    while running:
        elapsed_ms = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                game.on_key_down(pygame.key.name(event.key))

        accumulator += elapsed_ms
        speed = game.game["speed"] if game.game and "speed" in game.game else 100
        if accumulator > speed:
            accumulator = 0
            game.loop()

        game.draw()

        screen = pygame.display.get_surface()
        if game.game_over and screen is not None:
            show_game_over_overlay(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_loop()
