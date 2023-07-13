import tkinter as tk

class Grid:
    def __init__(self, window, size):
        self.size = size
        self.grid_labels = [[None] * size for _ in range(size)]
        self.players = [None] * 2  # Initialize a list to hold players
        self.robots = []  # Initialize the list of robots


        self.create_labels(window)
        self.create_players()
        self.create_robots()

        self.window = window
        self.window.bind('<KeyPress>', self.on_key_press)
        self.update_gui()

    def create_labels(self, window):
        for row in range(self.size):
            for col in range(self.size):
                label = tk.Label(window, width=8, height=2, relief=tk.RAISED, bg='black')
                label.grid(row=row, column=col)
                self.grid_labels[row][col] = label

    def create_players(self):
        player1 = Player(0, 0, 'green', self.size)
        player2 = Player(10, 0, 'blue', self.size)
        self.players[0] = player1  # Assign player1 to index 0
        self.players[1] = player2  # Assign player2 to index 1


    def create_robots(self):
        robot1 = Robot(10, 5, 'red', self.size)
        self.robots.append(robot1)

    def update_current_cell_color(self):
        for player in self.players:
            self.grid_labels[player.row][player.col].config(bg=player.color)
        for robot in self.robots:
            self.grid_labels[robot.row][robot.col].config(bg=robot.color)

    def reset_previous_cell_color(self):
        for player in self.players:
            self.grid_labels[player.row][player.col].config(bg='white')
        for robot in self.robots:
            self.grid_labels[robot.row][robot.col].config(bg='white')

    def check_collision(self, row, col):
        for player in self.players:
            if player.row == row and player.col == col:
                return True
        for robot in self.robots:
            if robot.row == row and robot.col == col:
                return True
        return False

    def on_key_press(self, event):
        self.reset_previous_cell_color()

        if event.char in ['w', 'a', 's', 'd']:
            player = self.players[0]  # Player 1 controls with WASD keys
        else:
            player = self.players[1]  # Player 2 controls with arrow keys

        new_row, new_col = player.get_new_position(event.keysym.lower())

        if not self.check_collision(new_row, new_col):
            player.move(new_row, new_col)

        self.update_current_cell_color()



    def update_gui(self):
        self.update_current_cell_color()
        self.window.after(100, self.update_gui)

class Player:
    def __init__(self, row, col, color, grid_size):
        self.row = row
        self.col = col
        self.color = color
        self.grid_size = grid_size

    def get_new_position(self, direction):
        new_row, new_col = self.row, self.col
        if direction == 'w' and self.row > 0:
            new_row -= 1
        elif direction == 's' and self.row < self.grid_size - 1:
            new_row += 1
        elif direction == 'a' and self.col > 0:
            new_col -= 1
        elif direction == 'd' and self.col < self.grid_size - 1:
            new_col += 1
        return new_row, new_col

    def move(self, new_row, new_col):
        self.row = new_row
        self.col = new_col

class Robot(Player):
    def __init__(self, row, col, color, grid_size):
        super().__init__(row, col, color, grid_size)
