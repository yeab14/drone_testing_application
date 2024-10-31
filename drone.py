# drone.py

class Drone:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.facing = None
        self.in_air = False
        self.directions = ["NORTH", "EAST", "SOUTH", "WEST"]

    def launch(self, x, y, facing):
        if 0 <= x < 5 and 0 <= y < 5 and facing in self.directions:
            self.x = x
            self.y = y
            self.facing = facing
            self.in_air = True
        else:
            print("Invalid launch command.")

    def fly(self):
        if self.in_air:
            if self.facing == "NORTH" and self.y < 4:
                self.y += 1
            elif self.facing == "EAST" and self.x < 4:
                self.x += 1
            elif self.facing == "SOUTH" and self.y > 0:
                self.y -= 1
            elif self.facing == "WEST" and self.x > 0:
                self.x -= 1
            else:
                print("Flight blocked: Out of bounds.")
    
    def left(self):
        if self.in_air:
            self.facing = self.directions[(self.directions.index(self.facing) - 1) % 4]

    def right(self):
        if self.in_air:
            self.facing = self.directions[(self.directions.index(self.facing) + 1) % 4]

    def status(self):
        if self.in_air:
            return f"{self.x},{self.y},{self.facing}"
        return "Drone is not in the air."
