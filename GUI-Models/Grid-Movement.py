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
        label = tk.Label(window, width=8, height=2, relief=tk.RAISED)
        label.grid(row=row, column=col)
        grid_labels[row][col] = label

# Initial position of the player
player = Player(0, 0, 'green')

# Function to update the current cell's color
def update_current_cell_color(player):
    for r in range(grid_size):
        for c in range(grid_size):
            if r == player.row and c == player.col:
                grid_labels[r][c].config(bg=player.color)
            else:
                grid_labels[r][c].config(bg='white')

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
        update_current_cell_color(player)
    elif event.keysym == 's' and player.row < grid_size - 1:
        player.row += 1
        update_current_cell_color(player)
    elif event.keysym == 'a' and player.col > 0:
        player.col -= 1
        update_current_cell_color(player)
    elif event.keysym == 'd' and player.col < grid_size - 1:
        player.col += 1
        update_current_cell_color(player)

# Bind keypress event to the window
window.bind('<KeyPress>', on_key_press)

# Run the GUI event loop
window.mainloop()
