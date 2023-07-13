import tkinter as tk

# Define grid size
grid_size = 20

# Define arrays for players and robots
players = []
robots = []

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
        
# Initial positions of players and robots
player1 = Player(0, 0, 'green')
player2 = Player(10, 0, 'blue')
robot1 = Robot(10, 5, 'red')

# Add players and robots to the arrays
players.append(player1)
players.append(player2)
robots.append(robot1)

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
def update_current_cell_color(players, robots):
    for player in players:
        grid_labels[player.row][player.col].config(bg=player.color)
    for robot in robots:
        grid_labels[robot.row][robot.col].config(bg=robot.color)

# Function to reset the previous cell's color
def reset_previous_cell_color(players, robots):
    for player in players:
        grid_labels[player.row][player.col].config(bg='white')
    for robot in robots:
        grid_labels[robot.row][robot.col].config(bg='white')


# Event handler for keypress events
def on_key_press(event):
    # Reset previous cell's color
    reset_previous_cell_color(players, robots)

    # Move player1 (controlled by WASD)
    if event.char in ['w', 'a', 's', 'd']:
        if event.char == 'w' and player1.row > 0:
            player1.row -= 1
        elif event.char == 's' and player1.row < grid_size - 1:
            player1.row += 1
        elif event.char == 'a' and player1.col > 0:
            player1.col -= 1
        elif event.char == 'd' and player1.col < grid_size - 1:
            player1.col += 1

    # Move player2 (controlled by arrow keys)
    elif event.keysym in ['Up', 'Down', 'Left', 'Right']:
        if event.keysym == 'Up' and player2.row > 0:
            player2.row -= 1
        elif event.keysym == 'Down' and player2.row < grid_size - 1:
            player2.row += 1
        elif event.keysym == 'Left' and player2.col > 0:
            player2.col -= 1
        elif event.keysym == 'Right' and player2.col < grid_size - 1:
            player2.col += 1

    # Update the current cell's color
    update_current_cell_color(players, robots)


# Bind keypress events to the window for player1 and player2
window.bind('<KeyPress-w>', on_key_press)
window.bind('<KeyPress-a>', on_key_press)
window.bind('<KeyPress-s>', on_key_press)
window.bind('<KeyPress-d>', on_key_press)

window.bind('<KeyPress-Up>', on_key_press)
window.bind('<KeyPress-Down>', on_key_press)
window.bind('<KeyPress-Left>', on_key_press)
window.bind('<KeyPress-Right>', on_key_press)

# Function to continuously update the GUI
def update_gui():
    update_current_cell_color(players, robots)
    window.after(100, update_gui)  # Update every 100 milliseconds

# Start updating the GUI
update_gui()

# Run the GUI event loop
window.mainloop()
