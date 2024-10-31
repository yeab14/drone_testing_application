class Drone:
    # Constants for cardinal directions
    NORTH = (0, 1)
    EAST = (1, 0)
    SOUTH = (0, -1)
    WEST = (-1, 0)

    # Movement mapping for rotation
    DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

    def __init__(self):
        self.x = 0  # Current x position
        self.y = 0  # Current y position
        self.direction_index = 0  # Facing NORTH initially
        self.in_air = False  # Drone starts off the ground

    def launch(self, x, y, direction):
        """Launch the drone to a specified position and direction."""
        if 0 <= x < 5 and 0 <= y < 5 and direction in ["NORTH", "EAST", "SOUTH", "WEST"]:
            self.x = x
            self.y = y
            self.direction_index = ["NORTH", "EAST", "SOUTH", "WEST"].index(direction)
            self.in_air = True

    def fly(self):
        """Move the drone forward in the current direction."""
        if self.in_air:
            dx, dy = self.DIRECTIONS[self.direction_index]
            new_x = self.x + dx
            new_y = self.y + dy
            
            if 0 <= new_x < 5 and 0 <= new_y < 5:
                self.x = new_x
                self.y = new_y

    def left(self):
        """Rotate the drone 90 degrees to the left."""
        if self.in_air:
            self.direction_index = (self.direction_index - 1) % 4

    def right(self):
        """Rotate the drone 90 degrees to the right."""
        if self.in_air:
            self.direction_index = (self.direction_index + 1) % 4

    def status(self):
        """Get the current status of the drone."""
        if self.in_air:
            direction = ["NORTH", "EAST", "SOUTH", "WEST"][self.direction_index]
            return (self.x, self.y, direction)
        else:
            return "Drone is not in the air."
    
    def execute_command(self, command):
        """Execute a command for the drone."""
        parts = command.split()
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
        return None

