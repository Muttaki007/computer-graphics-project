# Traffic Signal Simulation (PyOpenGL)

A simple 2D computer graphics project made with **Python**, **PyOpenGL** and **GLUT**.

Cars travel in two lanes (the lower lane moves right, the upper lane moves left) and obey a traffic signal that cycles through green, yellow and red. Cars stop at the stop line on red or yellow, wait in a queue, and move again on green.

## Features

- Two-way traffic with cars moving in opposite directions
- Traffic signal that changes automatically (green → yellow → red)
- Cars stop before the stop line and keep a safe gap from the car in front
- Cars appear at random time intervals, so the traffic looks natural
- Simple scene with sun, tree, house, grass and street

## Computer graphics concepts used

| Concept | Where it is used |
|---|---|
| Basic primitives (`GL_QUADS`, `GL_TRIANGLES`, `GL_TRIANGLE_FAN`) | Car, house, tree, signal, street |
| Parametric circle drawing (`cos`, `sin`) | Sun, wheels, signal lamps |
| Translation (`glPushMatrix`, `glTranslatef`, `glPopMatrix`) | Placing every object and moving the cars |
| Animation with `glutTimerFunc` | `update()` function runs every 15 ms |
| Double buffering (`GLUT_DOUBLE`, `glutSwapBuffers`) | Smooth, flicker-free animation |
| 2D projection (`gluOrtho2D`) | 800 x 500 coordinate system |

## How it works

1. **Signal:** the variable `light` stores the state (`0` = green, `1` = yellow, `2` = red). A counter changes the state after a fixed number of timer ticks.
2. **Cars:** each lane is a list, and every car is stored as `[x_position, color]`.
3. **Movement:** every tick a car moves by `SPEED` pixels. A car is blocked if
   - the light is not green and the car's front reaches the stop line, or
   - the car in front is too close.
4. **Spawning:** a new car enters a lane only when the entry point is free, after a random delay.

## Requirements

- Python 3
- PyOpenGL

```bash
pip install PyOpenGL PyOpenGL_accelerate
```

> On Windows, if GLUT does not work, install `freeglut` or download a PyOpenGL wheel that includes it.

## Run

```bash
python traffic_signal_opengl.py
```

## Customize

You can change these values at the top of the file:

| Variable | Meaning |
|---|---|
| `SPEED` | How fast the cars move |
| `GREEN_TIME`, `YELLOW_TIME`, `RED_TIME` | How long each light stays on (in timer ticks) |
| `CAR_W` | Width of a car |
| `randint(180, 320)` in `update()` | Time gap between new cars (bigger number = fewer cars) |

## Project structure

```
.
├── traffic_signal_opengl.py   # main program
├── screenshot.png             # screenshot of the output
└── README.md
```

## Future improvements

- Pedestrian crossing
- Keyboard control to change the signal manually
- Countdown timer on the signal
- Day and night mode
