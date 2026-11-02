# Traffic Signal Simulation

A 2D computer graphics project built with **Python** and **PyOpenGL**. It simulates a road with a working traffic signal, moving cars, and a simple outdoor scene (sun, tree, house, grass).

## Features

- Traffic signal that cycles automatically: Green → Yellow → Red
- Cars spawn at the left of the screen in random colors (red, blue, orange, purple)
- Cars stop at the stop line when the light is yellow or red
- Cars keep a safe distance from the car in front of them
- Cars are removed once they leave the screen
- Scenery: sun, tree, house, grass, road with a dashed center line

## How it works

| Part | Description |
|------|-------------|
| Signal timing | Green = 300 frames, Yellow = 100 frames, Red = 300 frames (one frame is about 15 ms) |
| Car spawning | A new car appears roughly every 120 frames if there is space at the start of the road |
| Car movement | Each car moves 2 pixels per frame unless it is blocked by the signal or the car ahead |
| Window size | 800 x 500 pixels |

## Computer graphics concepts used

- 2D orthographic projection (`gluOrtho2D`)
- Drawing primitives: `GL_QUADS`, `GL_TRIANGLES`, `GL_TRIANGLE_FAN`
- Geometric transformations (`glTranslatef`)
- Matrix stack (`glPushMatrix` / `glPopMatrix`)
- Double buffering (`glutSwapBuffers`)
- Animation using a timer callback (`glutTimerFunc`)
- Building complex objects (cars, house, tree, signal) from basic shapes

## Requirements

- Python 3.x
- PyOpenGL

Install the library with:

```
pip install PyOpenGL PyOpenGL_accelerate
```

> **Windows note:** If you get an error like `NullFunctionError: glutInit`, your system is missing the GLUT library. Install **freeglut** (or install a ready-made wheel, for example `pip install PyOpenGL-accelerate` along with the freeglut DLL placed in your Python folder or `System32`).

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```
python traffic_signal.py
```

(Replace `traffic_signal.py` with the actual name of your Python file.)

A window titled **Traffic Signal Simulation** will open and the animation starts automatically.

## Project structure

```
.
├── traffic_signal.py   # Main source code
└── README.md           # Project documentation
```

## Code overview

- `drawRectangle`, `drawTriangle`, `drawCircle`: basic shape helpers
- `drawCar`, `drawSignal`, `drawTree`, `drawHouse`: objects built from the basic shapes
- `drawScene`: draws the whole scene and every car
- `update`: runs every frame to change the light, spawn cars, move cars, and remove cars
- `showScreen`: display callback that clears the screen and draws the scene

## Author

**Abdullah Al Muttaki Khan**
Course: Computer Graphics
Institution: Bangladesh Army Univercity Of Science & Technology (BAUST)
