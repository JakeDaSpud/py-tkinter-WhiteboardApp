# Tutorial / guide: https://www.freecodecamp.org/news/build-a-whiteboard-app/

# Imports
import tkinter as tk
from tkinter.colorchooser import askcolor

# Create blank drawing / canvas
def start_drawing(event):
    # Global Variables
    global is_drawing, prev_x, prev_y

    is_drawing = True
    prev_x, prev_y = event.x, event.y # Mouse cursor position recorded

def draw(event):
    global is_drawing, prev_x, prev_y

    if is_drawing:
        current_x, current_y = event.x, event.y # Get cursor position to draw line there
        
        # TKinter function to make line using cursor position
        canvas.create_line(prev_x, prev_y, current_x, current_y, fill = drawing_color, width = line_width, capstyle = tk.ROUND, smooth = True)
        
        prev_x, prev_y = event.x, event.y # Mouse cursor position recorded

print("Exiting app.")