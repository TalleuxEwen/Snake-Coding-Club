# 🐍 Snake Workshop Documentation (Python version)

## 📌 Description
In this workshop, you will build the classic **Snake game** using Python and the [pygame](https://www.pygame.org/) library, running in its own window.
Along the way, you'll learn core programming concepts such as variables, functions, dictionaries, and inputs.

By the end, you'll have:
- A fully playable game
- A better understanding of how interactive programs work

**Language used:** Python

---

## 🧰 Prerequisites
- A laptop *(can be provided during offline sessions)*
- Python 3.9+ installed
- A code editor such as [Visual Studio Code](https://code.visualstudio.com/Download) or similar
- The project repository downloaded and ready
- The `pygame` library installed (`pip install -r requirements.txt`)

---

## ⚠️ Before you start
At the end of this document, you will see a list of functions and variables already set up for you to use in this project, don't forget to use them!

## 🚀 Steps

### 1. Draw Gameboard
**Concept:** Functions

Create a function that draws the game area (grid) where the snake will move.

**You'll learn:**
- How to define and call a function

---

### 2. Store Gameboard Variables
**Concept:** Variables

Define variables for properties like:
- Width and height of the board
- Colors of game elements

**You'll learn:**
- How to store and reuse values
- Why variables make code flexible and easier to change

---

### 3. Draw a Single Square
**Concept:** Using variables

Create a function to draw one square on the board using coordinates.

**You'll learn:**
- How to create functions with parameters
- How small functions can be reused to build bigger features

---

### 4. Create a Snake Object
**Concept:** Dictionaries

Represent the snake as a dictionary that contains:
- Its position (list of body parts)
- Its direction
- Its length

**You'll learn:**
- How to group related data
- Why dictionaries are useful for modeling real things in code

---

### 5. Draw Snake
**Concept:** Working with dictionaries and lists

Use the snake dictionary to draw each part of the snake on the board.

**You'll learn:**
- How to use lists to store multiple informations

---

### 6. Read User Input
**Concept:** `if` conditions

Capture keyboard input (arrow keys) and change the snake's direction.

**You'll learn:**
- How to handle user input
- How to use conditional logic (`if`) to control behavior

---

### 7. Snake Movement
**Concepts:** Functions & multiple conditions

Update the snake's position over time:
- Move the head forward
- Shift the body

---

### 8. Snake Movement at Edges
**Concept:** `else` conditions

Define what happens when the snake reaches the edge:
- Wrap around **or**
- Stop the game

**You'll learn:**
- How to handle edge cases
- How `if` / `else` structures control different outcomes

---

### 9. Spawn Fruit

Generate a fruit at a random position on the board.

---

### 10. Snake–Fruit Interaction

Check if the snake eats the fruit.

---

### 11. Update Score

Increase and display the score when the snake eats fruit.

---

### 12. Stop the Game

End the game when:
- The snake hits itself
- (Or another defined condition)

---

## 🧩 Available Functions

These functions are provided to allow you to perform certain actions, such as drawing visuals in the game or certain logics.

You are free to use them.

```python
def draw_board(width, height, colour)
# Draws the gameboard with given dimensions and color

def draw_square(x, y, colour)
# Draws a single square at a specific position

def draw_score(score)
# Displays the current score on screen

def draw_snake_body(snake_body, snake_body_colour, snake_length)
# Draws the snake using its body list and length

def get_random_number(min_value, max_value)
# Returns a random number between min and max (used for fruit spawning)

def snake_body_movement(snake_body, snake_length, snake_head, fruit_eaten)
# Updates the snake's body positions and handles growth when fruit is eaten
```

## 🔧 Available Variables

```python
# Arrow keys (keyboard input values)

ARROW_UP = "up"
# Triggered when the up arrow key is pressed

ARROW_DOWN = "down"
# Triggered when the down arrow key is pressed

ARROW_RIGHT = "right"
# Triggered when the right arrow key is pressed

ARROW_LEFT = "left"
# Triggered when the left arrow key is pressed


# Directions (used for snake movement logic)

UP = "Up"
# Represents upward movement

RIGHT = "Right"
# Represents movement to the right

DOWN = "Down"
# Represents downward movement

LEFT = "Left"
# Represents movement to the left
```

These functions and variables are provided in `workshop_functions.py` and `workshop_constants.py`. To use them in `game.py`, import them at the top of the file, for example:

```python
from workshop_functions import draw_board, draw_square, draw_score, draw_snake_body, get_random_number, snake_body_movement
from workshop_constants import ARROW_UP, ARROW_DOWN, ARROW_LEFT, ARROW_RIGHT, UP, DOWN, LEFT, RIGHT
```

## 💡 Don't worry if everything doesn't work immediately, debugging is part of programming.
