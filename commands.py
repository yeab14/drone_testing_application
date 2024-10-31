# commands.py

from drone import Drone

def process_commands(commands):
    drone = Drone()
    output = []
    
    for command in commands:
        parts = command.split()
        if parts[0] == "LAUNCH":
            x, y, facing = map(str.strip, parts[1].split(","))
            drone.launch(int(x), int(y), facing)
        elif parts[0] == "FLY":
            drone.fly()
        elif parts[0] == "LEFT":
            drone.left()
        elif parts[0] == "RIGHT":
            drone.right()
        elif parts[0] == "STATUS":
            output.append(drone.status())
    
    return output
