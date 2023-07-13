import tkinter as tk
from grid import Grid

# Create Tkinter window
window = tk.Tk()
window.title("Grid Search GUI")

# Create grid
grid_size = 20
grid = Grid(window, grid_size)

# Run the GUI event loop
window.mainloop()
