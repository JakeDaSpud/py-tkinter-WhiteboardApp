# Tutorial / guide: https://www.freecodecamp.org/news/build-a-whiteboard-app/

# Imports
import tkinter as tk
from tkinter.colorchooser import askcolor

def start_drawing(event):
    """
    Set is_drawing to True
    @param: event The mouse input data
    """

    global is_drawing, prev_x, prev_y

    is_drawing = True
    prev_x, prev_y = event.x, event.y # Mouse cursor position recorded

def stop_drawing(event):
    """
    Set is_drawing to False
    @param: event The mouse input data
    """

    global is_drawing

    is_drawing = False

def draw(event):
    """
    Draw coloured vectors to canvas
    @param: event The mouse input data
    """

    global is_drawing, prev_x, prev_y

    if is_drawing:
        current_x, current_y = event.x, event.y # Get cursor position to draw line there
        
        # TKinter function to make line using cursor position
        canvas.create_line(prev_x, prev_y, current_x, current_y, fill = drawing_color, width = line_width, capstyle = tk.ROUND, smooth = True)
        
        prev_x, prev_y = event.x, event.y # Mouse cursor position recorded

def change_pen_color():
    """
    Use tkinter's askcolor() to change canvas pen colour
    """

    global drawing_color
    
    color = askcolor()[1] # askcolor() is from tkinter to change canvas pen colour
    if color: # Not null
        drawing_color = color

def change_line_width(value):
    """
    Change tkinter's canvas pen thickness
    @param: value New canvas pen size
    """

    global line_width
    line_width = int(value)

print("Exiting WhiteboardApp, goodbye!")
