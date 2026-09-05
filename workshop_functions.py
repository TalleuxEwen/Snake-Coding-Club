#
# /!\ PLEASE DO NOT MODIFY THE CONTENT OF THIS DOCUMENT /!\
#

import math
import random

import pygame


#
# Draw functions
#

def _to_colour(colour):
    if isinstance(colour, str):
        return pygame.Color(colour)
    return colour


def draw_square(x, y, colour):
    screen = pygame.display.get_surface()
    if screen is None:
        return
    import game
    square_size = game.SQUARE_SIZE
    rect = pygame.Rect(x * square_size, y * square_size, square_size, square_size)
    pygame.draw.rect(screen, _to_colour(colour), rect)


def draw_board(width, height, colour):
    import game

    screen = pygame.display.get_surface()
    screen.fill(_to_colour(colour))


def draw_score(score):
    screen = pygame.display.get_surface()
    if screen is None:
        return
    font = pygame.font.SysFont(None, 28)
    text = font.render("Score " + str(score), True, pygame.Color("white"))
    screen.blit(text, (5, 5))


def draw_snake_body(snake_body, snake_body_colour, snake_length):
    for i in range(1, snake_length):
        draw_square(snake_body[i]["x"], snake_body[i]["y"], snake_body_colour)


#
# Snake logic functions
#

def snake_body_movement(snake_body, snake_length, snake_head, fruit_eaten):
    snake_body.insert(0, {"x": snake_head["x"], "y": snake_head["y"]})
    if fruit_eaten is False:
        snake_body.pop()
    if snake_bite_body(snake_body, snake_head, snake_length) is True:
        import game
        game.game["status"] = "stop"
        show_game_over()


def snake_bite_body(snake_body, snake_head, snake_length):
    for i in range(1, snake_length):
        if snake_body[i]["x"] == snake_head["x"] and snake_body[i]["y"] == snake_head["y"]:
            return True
    return False


def show_game_over():
    import game
    game.game_over = True


def get_random_number(min_value, max_value):
    return math.floor(random.random() * max_value) + min_value
