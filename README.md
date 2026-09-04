# SnakeCodingClub

This is the Snake Coding Club workshop, built in Python using the [pygame](https://www.pygame.org/) library.

Further information about the project can be found in the [Documentation](doc/Documentation.md).
There is also a small tutorial here: [Tutorial](doc/IntroductionTutorial.md).

---

## 1. Download the project

Download or clone this folder onto your computer.

---

## 2. Install Python

Make sure you have Python 3.9 or newer installed.

### Windows

1. Go to [python.org/downloads](https://www.python.org/downloads/) and click **Download Python**.
2. Run the installer.
3. ⚠️ **Important:** on the first installer screen, check the box **"Add python.exe to PATH"** at the bottom before clicking **Install Now**. If you skip this, the commands below won't work.
4. Once installed, open a terminal: press `Win`, type `cmd`, and press Enter.
5. Check the installation with:
   ```text
   python --version
   ```
   (on Windows, the command is usually `python`, not `python3`)

### macOS

1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the macOS installer.
2. Run the installer and follow the steps.
3. Open a terminal: press `Cmd + Space`, type `Terminal`, and press Enter.
4. Check the installation with:
   ```text
   python3 --version
   ```

If the command isn't recognized on either OS, close and reopen your terminal, or restart your computer, then try again.

---

## 3. Install the dependencies

In your terminal, navigate to the project folder. For example, if you downloaded it to your `Downloads` folder:

```text
cd Downloads/Coding-Club-Snake-Python
```

### Create a virtual environment

A virtual environment keeps this project's dependencies separate from the rest of your system. This is required on some systems (e.g. macOS with Python installed via Homebrew) and is good practice everywhere.

**Windows:**
```text
python -m venv venv
venv\Scripts\activate
```

**macOS:**
```text
python3 -m venv venv
source venv/bin/activate
```

You should now see `(venv)` at the start of your terminal prompt. You'll need to run the `activate` command again each time you open a new terminal to work on this project.

### Install pygame

With the virtual environment active, run:

```text
pip install -r requirements.txt
```

This installs `pygame`, the library used to draw the game window and read the keyboard.

---

## 4. Open the project in your editor

Open Visual Studio Code (or any other editor):

1. Click **File**
2. Click **Open Folder**
3. Select this project folder

---

## 5. Run the game

Make sure your virtual environment is active (you should see `(venv)` in your prompt — if not, run the `activate` command from step 3 again).

From a terminal inside the project folder, run:

```text
python3 main.py
```

(on Windows, use `python main.py` if `python3` is not recognized)

A window should open. As long as `game.py` is empty, nothing will be drawn yet — that's normal, it's your job to fill it in!

### Troubleshooting

- **`python3: command not found` / `'python' is not recognized`** — Python isn't installed correctly, or wasn't added to PATH. Reinstall and make sure to check the PATH option (Windows) or restart your terminal.
- **`ModuleNotFoundError: No module named 'pygame'`** — the dependencies weren't installed. Re-run `pip install -r requirements.txt` from inside the project folder.
- **`No such file or directory: main.py`** — you're not in the right folder. Use `cd` to navigate into the project folder first (see step 3).
- **`error: externally-managed-environment`** — you tried to `pip install` without activating the virtual environment. Go back to step 3 and run the `activate` command, then try again.

---

## 6. Start coding

Open `game.py` and start filling in the `loop()`, `draw()` and `on_key_down()` functions, following the [Documentation](doc/Documentation.md).
