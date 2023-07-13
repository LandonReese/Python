import tkinter as tk

# Define grid size
grid_size = 20

# Define Player struct
class Player:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

# Define Robot struct
class Robot(Player):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

# Create Tkinter window
window = tk.Tk()
window.title("Grid Search GUI")

# Create grid using labels
grid_labels = [[None] * grid_size for _ in range(grid_size)]
for row in range(grid_size):
    for col in range(grid_size):
        label = tk.Label(window, width=8, height=2, relief=tk.RAISED, bg='black')
        label.grid(row=row, column=col)
        grid_labels[row][col] = label

# Initial position of the player
player = Player(0, 0, 'red')

# Function to update the current cell's color
def update_current_cell_color(player):
    grid_labels[player.row][player.col].config(bg=player.color)

# Function to reset the previous cell's color
def reset_previous_cell_color(player):
    grid_labels[player.row][player.col].config(bg='white')

# Event handler for keypress events
def on_key_press(event):
    # Reset previous cell's color
    reset_previous_cell_color(player)

    # Move the player based on the pressed key
    if event.keysym == 'w' and player.row > 0:
        player.row -= 1
    elif event.keysym == 's' and player.row < grid_size - 1:
        player.row += 1
    elif event.keysym == 'a' and player.col > 0:
        player.col -= 1
    elif event.keysym == 'd' and player.col < grid_size - 1:
        player.col += 1
    
    # Update the current cell's color
    update_current_cell_color(player)

# Bind keypress event to the window
window.bind('<KeyPress>', on_key_press)

# Function to continuously update the GUI
def update_gui():
    update_current_cell_color(player)
    window.after(100, update_gui)  # Update every 100 milliseconds

# Start updating the GUI
update_gui()

# Run the GUI event loop
window.mainloop()
