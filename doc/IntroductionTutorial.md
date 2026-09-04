# Introduction to programming in Python and Project Tutorial

This project is the starting point of a small Snake game. Some parts of the game are already handled for you, such as the functions to draw on the screen.

This document presents how variables and functions work in Python in order to get started.

It is highly encouraged to go and find resources online or on other websites that contain tutorials on Python and programming in general.

---

## Variables: storing data

A **variable** is used to store data that your program can use later.

In Python, variables are created simply by assigning a value to a name.

```python
SQUARE_SIZE = 25
```

This line can be separated into multiple parts:

- `SQUARE_SIZE` is the name of the variable
- `=` assigns a value to the variable
- `25` is the stored value

---

### Choosing a variable name

Variable names should describe what the value represents.

Example:

```python
player_speed = 10
snake_length = 5
game_over = False
```

A clear variable name makes code easier to read and understand.

---

### Constants versus variables that change

Python does not have a real `const` keyword. By convention, variables that are not meant to change are written in `ALL_CAPS`:

```python
SQUARE_SIZE = 25
```

Variables that are meant to change during the game are written in `snake_case`:

```python
score = 0

score = score + 10
```

Here, the value stored in `score` changes over time.

---

### Variables can also store dictionaries

A variable can store more than a single value.

```python
game = {
    "status": "playing",
    "score": 0,
    "speed": 100,
}
```

This is called a **dictionary**.

Inside the dictionary:

- `"status"` stores the current game state
- `"score"` stores the player's score
- `"speed"` stores the game speed

You can access these values like this:

```python
game["score"] = game["score"] + 10
```

This example code increases the score by 10.

---

## Functions: reusable blocks of code

A **function** is a reusable block of code that performs a task.

Functions are useful because they allow the same code to be executed multiple times without rewriting it.

Here is a complete example:

```python
result = 0  # An external variable in the context of this example

def add_numbers(a, b):
    global result
    result = a + b
```

This function can be separated into several parts:

- `def` tells Python that a function is being created
- `add_numbers` is the name of the function
- `a` and `b` are called **parameters**
- the indented block contains the code that will run when the function is called

The parameters (`a` and `b`) are variables created by the function itself.
They receive values when the function is called.

Example:

```python
add_numbers(5, 3)
```

When this function call happens:

- `a` receives the value `5`
- `b` receives the value `3`

So inside the function, the code becomes:

```python
result = 5 + 3
```

After the calculation, `result` will contain `8`.

This allows the same function to work with different values without rewriting the logic every time.

For example:

```python
add_numbers(10, 2)
add_numbers(7, 1)
add_numbers(100, 50)
```

Each function call uses different values while reusing the same code structure.

---

### Functions in this project

Some functions are already provided for you and will automatically be called by the game system:

```python
def loop():
    pass

def draw():
    pass

def on_key_down(key_code):
    pass
```

Each function has a specific purpose:

- `loop()` updates the game logic repeatedly
- `draw()` renders the game on the screen
- `on_key_down(key_code)` reacts to keyboard input

The `key_code` parameter contains information about the pressed key.

This value can either be:

```python
ARROW_UP
ARROW_DOWN
ARROW_RIGHT
ARROW_LEFT
```

⚠️ Check the provided documentation to see which predefined variables and key codes are available.

---
