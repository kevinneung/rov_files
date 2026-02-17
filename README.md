# ROV Joystick Control System

Arduino-based joystick control system for a Remote Operated Vehicle (ROV) with real-time Python visualization dashboards.

## Overview

This project reads analog joystick input and a digital button from an Arduino, transmits the data over serial, and visualizes it in real-time on a PC using either a Pygame or Tkinter dashboard.

```
Arduino (Joystick + Button)
        |
        | Serial (COM3, 9600 baud)
        | Format: "X: 512 | Y: 512 | Button: 1"
        |
   +-----------+-----------+
   |                       |
dashboard.py    tklinter_joystick_dashboard.py
 (Pygame)              (Tkinter)
```

## Files

### `main.cpp` — Arduino Firmware

Reads joystick X/Y axes (analog pins A0, A1) and a button (digital pin 2) and sends formatted data over serial at 9600 baud every 100ms.

### `dashboard.py` — Pygame Dashboard

Real-time 400x400 visualization using Pygame. Displays the joystick position as a dot within a circular boundary with crosshairs. The dot turns red when the button is pressed.

### `tklinter_joystick_dashboard.py` — Tkinter Dashboard

Lightweight alternative using Python's built-in Tkinter library. Same visualization as the Pygame version, plus a text readout of raw X, Y, and button values.

## Hardware Setup

- **X-axis** — Analog pin A0
- **Y-axis** — Analog pin A1
- **Button** — Digital pin 2 (internal pull-up)

## Requirements

- Arduino board with an analog joystick module
- Python 3 with `pyserial`
- `pygame` (for `dashboard.py`) or Tkinter (included with Python)

## Usage

1. Upload `main.cpp` to the Arduino.
2. Connect via USB (defaults to COM3).
3. Run either dashboard:
   ```bash
   python dashboard.py
   # or
   python tklinter_joystick_dashboard.py
   ```
