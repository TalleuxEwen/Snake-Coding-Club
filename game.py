#
# This is where you can code your game and the logic
# You can write inside the functions, create new functions and variables or modify the variables
#
# /!\ Do not modify the actual structures of the functions, otherwise it will not work /!\
#


#
# variables
#

# size of square tiles in pixels
SQUARE_SIZE = 25

# Informations about the game status
game = {
    "status": "playing",
    "score": 0,
    "speed": 100,
}

# Set to True to display the "GAME OVER" overlay
game_over = False


#
# Functions
#

# This function is automatically called every frame
# It is used to update the game state (movement, logic, collisions, etc.)
def loop():
    pass


# This function is automatically called every frame
# It is used to render (draw) everything on the screen
def draw():
    pass


# This function is called whenever a key is pressed
# The key_code parameter tells which key was pressed
def on_key_down(key_code):
    pass
