import pygame
import serial
import sys

# Serial setup
ser = serial.Serial('COM3', 9600, timeout=0.01)

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Joystick Visualizer")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 80, 80)
DARK_GRAY = (100, 100, 100)

# Joystick state
x_val, y_val, button = 512, 512, 1

def parse_serial(line):
    """Parse Arduino output: 'X: 512 | Y: 512 | Button: 1'"""
    try:
        parts = line.split(' | ')
        x = int(parts[0].split(': ')[1])
        y = int(parts[1].split(': ')[1])
        btn = int(parts[2].split(': ')[1])
        return x, y, btn
    except:
        return None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read serial data
    if ser.in_waiting > 0:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                parsed = parse_serial(line)
                if parsed:
                    x_val, y_val, button = parsed
        except:
            pass

    # Map Arduino values (0-1023) to screen coordinates (50-350)
    screen_x = int((x_val / 1023) * 300 + 50)
    screen_y = int((y_val / 1023) * 300 + 50)

    # Draw
    screen.fill(WHITE)
    
    # Draw boundary circle
    pygame.draw.circle(screen, GRAY, (200, 200), 150, 2)
    
    # Draw crosshairs
    pygame.draw.line(screen, GRAY, (200, 50), (200, 350), 1)
    pygame.draw.line(screen, GRAY, (50, 200), (350, 200), 1)
    
    # Draw joystick position (color changes when button pressed)
    color = RED if button == 0 else DARK_GRAY
    pygame.draw.circle(screen, color, (screen_x, screen_y), 15)

    pygame.display.flip()
    clock.tick(60)

ser.close()
pygame.quit()
sys.exit()