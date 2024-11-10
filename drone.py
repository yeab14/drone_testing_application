import json  
import os  

class Drone:  
    # Constants for directions  
    NORTH = (0, 1)  
    EAST = (1, 0)  
    SOUTH = (0, -1)  
    WEST = (-1, 0)  

    DIRECTIONS = [NORTH, EAST, SOUTH, WEST]  
    DIRECTION_NAMES = ["NORTH", "EAST", "SOUTH", "WEST"]  

    def __init__(self, width=5, height=5):  
        """Initialize the drone with a given width and height."""  
        self.x = 0   
        self.y = 0  
        self.direction_index = 0   
        self.in_air = False   
        self.width = width  
        self.height = height  
        self.command_history = []  

    def launch(self, x, y, direction):  
        """Launch the drone to a specified position and direction."""  
        if not (0 <= x < self.width and 0 <= y < self.height):  
            return "Invalid launch coordinates. Please stay within bounds."  
        
        if direction not in self.DIRECTION_NAMES:  
            return "Invalid direction. Please use NORTH, EAST, SOUTH, or WEST."  

        self.x = x  
        self.y = y  
        self.direction_index = self.DIRECTION_NAMES.index(direction)  
        self.in_air = True  
        self.log_command(f"LAUNCH {x},{y},{direction}")  

    def fly(self):  
        """Fly the drone forward in the current direction."""  
        if not self.in_air:  
            return "Drone is not in the air."  

        if self.direction_index == 0:  # NORTH  
            if self.y < self.height - 1:  
                self.y += 1  
            else:  
                return "Cannot fly out of bounds."  
        elif self.direction_index == 1:  # EAST  
            if self.x < self.width - 1:  
                self.x += 1  
            else:  
                return "Cannot fly out of bounds."  
        elif self.direction_index == 2:  # SOUTH  
            if self.y > 0:  
                self.y -= 1  
            else:  
                return "Cannot fly out of bounds."  
        elif self.direction_index == 3:  # WEST  
            if self.x > 0:  
                self.x -= 1  
            else:  
                return "Cannot fly out of bounds."  

    def left(self):  
        """Rotate the drone 90 degrees to the left."""  
        if self.in_air:  
            self.direction_index = (self.direction_index - 1) % 4  
            self.log_command("LEFT")  
        else:  
            return "Drone is not in the air. Please launch the drone first."  

    def right(self):  
        """Rotate the drone 90 degrees to the right."""  
        if self.in_air:  
            self.direction_index = (self.direction_index + 1) % 4  
            self.log_command("RIGHT")  
        else:  
            return "Drone is not in the air. Please launch the drone first."  

    def status(self):  
        """Get the current status of the drone."""  
        if self.in_air:  
            direction = self.DIRECTION_NAMES[self.direction_index]  
            return (self.x, self.y, direction)  
        else:  
            return "Drone is not in the air."  

    def execute_command(self, command):  
        """Execute a command for the drone and log it."""  
        parts = command.split()  
        if not self.in_air and parts[0] != "LAUNCH":  
            return "Drone is not in the air. Please launch the drone first."  

        if parts[0] == "LAUNCH":  
            try:  
                x, y, direction = map(str.strip, parts[1].split(","))  
                return self.launch(int(x), int(y), direction)  
            except ValueError:  
                return "Invalid launch command format. Use: LAUNCH x,y,DIRECTION"  
        elif parts[0] == "FLY":  
            return self.fly()  
        elif parts[0] == "LEFT":  
            return self.left()  
        elif parts[0] == "RIGHT":  
            return self.right()  
        elif parts[0] == "STATUS":  
            return self.status()  
        else:  
            return "Invalid command. Please enter a valid command."  

        self.command_history.append(command)  

    def log_command(self, command):  
        """Log the command to a history file."""  
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
        else:  
            return "State file does not exist."