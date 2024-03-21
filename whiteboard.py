# Tutorial / guide: https://www.freecodecamp.org/news/build-a-whiteboard-app/

# Imports
import tkinter as tk
from tkinter.colorchooser import askcolor

# Python Functions

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

def draw(event, drawing_color):
    """
    Draw coloured vectors to canvas
    @param: event The mouse input data
    @param: drawing_color The colour to draw on canvas
    """

    global is_drawing, prev_x, prev_y

    if is_drawing:
        current_x, current_y = event.x, event.y # Get cursor position to draw line there
        
        # TKinter function to make line using cursor position
        canvas.create_line(prev_x, prev_y, current_x, current_y, fill = drawing_color, width = line_width, capstyle = tk.ROUND, smooth = True)
        
        prev_x, prev_y = event.x, event.y # Mouse cursor position recorded

def change_pen_color():
    """
    Use Tkinter's askcolor() to change canvas pen colour
    """

    global drawing_color
    
    color = askcolor()[1] # askcolor() is from Tkinter to change canvas pen colour
    if color: # Not null
        drawing_color = color

def change_line_width(value):
    """
    Change Tkinter's canvas pen thickness
    @param: value New canvas pen size
    """

    global line_width
    line_width = int(value)

# TODO
def set_theme(new_background_colour, new_pen_colour):
    """
    Function
    @param: 
    """
    # change background colour of window / colour whole canvas in

    # change canvas pen colour

# Tkinter Functions

root = tk.Tk() # Initialise object
root.title("Jake's MS-Pain") # Set (window) title

is_drawing = False
drawing_color = "thistle"
background_colour = "sea green"
line_width = 50

canvas = tk.Canvas(root, bg = background_colour) # Add canvas component to "root" tk, with green bg
canvas.pack(fill = "both", expand = True) # Make canvas fill horizontal and vertical window space

# 6 * (160x144) - the Gameboy's resolution!
root.geometry("960x864") # Window size in pixels: w x h

# UI Elements (Navbar and Controls)

controls_frame = tk.Frame(root) # Add Frame Component to Window
controls_frame.pack(side = "top", fill = "x") # Layout frame to top position Window

# Frame button which changes canvas pen colour
color_button = tk.Button(controls_frame, text = "Change Colour", command = change_pen_color)
# Frame button to clear / reset canvas
clear_button = tk.Button(controls_frame, text = "Clear Canvas", command = lambda: canvas.delete("all"))

color_button.pack(side = "left", padx=5, pady=5) # Layout button
clear_button.pack(side = "left", padx=5, pady=5) # Layout button

# Label is just text
line_width_label = tk.Label(controls_frame, text = "Line Width:")
line_width_label.pack(side = "left", padx=5, pady=5)

# Scale is slider widget, from 1 to 10
line_width_slider = tk.Scale(controls_frame, from_=1, to=10, orient = "horizontal", command = lambda val: change_line_width(val))
line_width_slider.set(line_width) # Set slider with initial value from earlier
line_width_slider.pack(side = "left", padx=5, pady=5)

# TODO
# Add 3/4 buttons with themes: sets the background-colour + pen colour

# Binding events / functions to GUI
canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", lambda event: draw(event, drawing_color))
canvas.bind("<ButtonRelease-1>", stop_drawing)

# Erasing function
canvas.bind("<Button-3>", start_drawing)
canvas.bind("<B3-Motion>", lambda event: draw(event, background_colour))
canvas.bind("<ButtonRelease-3>", stop_drawing)


root.mainloop() # Runs actual app

print("Closing Jake's MS-Pain, goodbye!")
