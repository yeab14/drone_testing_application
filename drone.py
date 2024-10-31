import json
import os

class Drone:
    # Constants for cardinal directions
    NORTH = (0, 1)
    EAST = (1, 0)
    SOUTH = (0, -1)
    WEST = (-1, 0)

    # Movement mapping for rotation
    DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

    def __init__(self, width=5, height=5):
        self.x = 0  # Current x position
        self.y = 0  # Current y position
        self.direction_index = 0  # Facing NORTH initially
        self.in_air = False  # Drone starts off the ground
        self.width = width
        self.height = height
        self.command_history = []

    def launch(self, x, y, direction):
        """Launch the drone to a specified position and direction."""
        if 0 <= x < self.width and 0 <= y < self.height and direction in ["NORTH", "EAST", "SOUTH", "WEST"]:
            self.x = x
            self.y = y
            self.direction_index = ["NORTH", "EAST", "SOUTH", "WEST"].index(direction)
            self.in_air = True
            self.log_command(f"LAUNCH {x},{y},{direction}")

    def fly(self):
        """Move the drone forward in the current direction."""
        if self.in_air:
            dx, dy = self.DIRECTIONS[self.direction_index]
            new_x = self.x + dx
            new_y = self.y + dy
            
            if 0 <= new_x < self.width and 0 <= new_y < self.height:
                self.x = new_x
                self.y = new_y
                self.log_command("FLY")

    def left(self):
        """Rotate the drone 90 degrees to the left."""
        if self.in_air:
            self.direction_index = (self.direction_index - 1) % 4
            self.log_command("LEFT")

    def right(self):
        """Rotate the drone 90 degrees to the right."""
        if self.in_air:
            self.direction_index = (self.direction_index + 1) % 4
            self.log_command("RIGHT")

    def status(self):
        """Get the current status of the drone."""
        if self.in_air:
            direction = ["NORTH", "EAST", "SOUTH", "WEST"][self.direction_index]
            return (self.x, self.y, direction)
        else:
            return "Drone is not in the air."

    def execute_command(self, command):
        """Execute a command for the drone and log it."""
        parts = command.split()
        if not self.in_air and parts[0] != "LAUNCH":
            return "Drone is not in the air. Please launch the drone first."

        if parts[0] == "LAUNCH":
            x, y, direction = map(str.strip, parts[1].split(","))
            self.launch(int(x), int(y), direction)
        elif parts[0] == "FLY":
            self.fly()
        elif parts[0] == "LEFT":
            self.left()
        elif parts[0] == "RIGHT":
            self.right()
        elif parts[0] == "STATUS":
            return self.status()
        else:
            return "Invalid command. Please enter a valid command."

        # After executing the command, log the command to the history
        self.command_history.append(command)

    def log_command(self, command):
        with open("history.txt", "a") as log_file:
            log_file.write(command + "\n")

    def save_state(self, filename="drone_state.json"):
        """Save the current state of the drone."""
        state = {
            'x': self.x,
            'y': self.y,
            'direction_index': self.direction_index,
            'in_air': self.in_air
        }
        with open(filename, "w") as f:
            json.dump(state, f)

    def load_state(self, filename="drone_state.json"):
        """Load the state of the drone from a file."""
        if os.path.exists(filename):
            with open(filename, "r") as f:
                state = json.load(f)
                self.x = state['x']
                self.y = state['y']
                self.direction_index = state['direction_index']
                self.in_air = state['in_air']
