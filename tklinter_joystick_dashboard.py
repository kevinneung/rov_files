import tkinter as tk
import serial

# Serial setup
ser = serial.Serial('COM3', 9600, timeout=0.01)

# Tkinter setup
root = tk.Tk()
root.title("Joystick Visualizer")
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Draw static elements
canvas.create_oval(50, 50, 350, 350, outline='gray', width=2)  # Boundary
canvas.create_line(200, 50, 200, 350, fill='gray')  # Vertical crosshair
canvas.create_line(50, 200, 350, 200, fill='gray')  # Horizontal crosshair

# Joystick dot
dot = canvas.create_oval(190, 190, 210, 210, fill='gray', outline='')

# Text display
text = canvas.create_text(200, 380, text="X: 512 | Y: 512 | Button: 1", font=('Arial', 10))

def parse_serial(line):
    try:
        parts = line.split(' | ')
        x = int(parts[0].split(': ')[1])
        y = int(parts[1].split(': ')[1])
        btn = int(parts[2].split(': ')[1])
        return x, y, btn
    except:
        return None

def update():
    if ser.in_waiting > 0:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                parsed = parse_serial(line)
                if parsed:
                    x_val, y_val, button = parsed
                    
                    # Map to screen coordinates
                    screen_x = int((x_val / 1023) * 300 + 50)
                    screen_y = int((y_val / 1023) * 300 + 50)
                    
                    # Update dot position
                    canvas.coords(dot, screen_x-10, screen_y-10, screen_x+10, screen_y+10)
                    
                    # Change color on button press
                    color = 'red' if button == 0 else 'gray'
                    canvas.itemconfig(dot, fill=color)
                    
                    # Update text
                    canvas.itemconfig(text, text=f"X: {x_val} | Y: {y_val} | Button: {button}")
        except:
            pass
    
    root.after(16, update)  # ~60 FPS

update()
root.mainloop()
ser.close()