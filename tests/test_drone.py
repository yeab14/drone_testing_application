import sys
import os
import unittest

# Ensure the drone module can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from drone import Drone

class TestDrone(unittest.TestCase):
    def test_launch_valid(self):
        drone = Drone()
        drone.launch(0, 0, "NORTH")
        self.assertEqual(drone.status(), (0, 0, "NORTH"))

    def test_fly(self):
        drone = Drone()
        drone.launch(0, 0, "EAST")
        drone.fly()
        self.assertEqual(drone.status(), (1, 0, "EAST"))

    def test_fly_out_of_bounds(self):
        drone = Drone()
        drone.launch(4, 4, "EAST")
        drone.fly()  # Should not move out of bounds
        self.assertEqual(drone.status(), (4, 4, "EAST"))

    def test_rotate_left(self):
        drone = Drone()
        drone.launch(0, 0, "NORTH")
        drone.left()
        self.assertEqual(drone.status(), (0, 0, "WEST"))

    def test_rotate_right(self):
        drone = Drone()
        drone.launch(0, 0, "NORTH")
        drone.right()
        self.assertEqual(drone.status(), (0, 0, "EAST"))

    def test_status_when_not_in_air(self):
        drone = Drone()
        self.assertEqual(drone.status(), "Drone is not in the air.")

    def test_save_load_state(self):
        drone = Drone()
        drone.launch(1, 1, "SOUTH")
        drone.save_state()
        new_drone = Drone()
        new_drone.load_state()
        self.assertEqual(new_drone.status(), (1, 1, "SOUTH"))

    # New Test: Verifying STATUS command output
    def test_status(self):
        drone = Drone()
        drone.launch(2, 2, "WEST")
        result = drone.status()
        expected = (2, 2, "WEST")
        self.assertEqual(result, expected)
        print(f"Test Status Result: {result}") 

    def test_ignore_invalid_commands(self):
        drone = Drone()
        # Before launch, any command should be ignored
        self.assertEqual(drone.execute_command("FLY"), "Drone is not in the air. Please launch the drone first.")
        self.assertEqual(drone.execute_command("LEFT"), "Drone is not in the air. Please launch the drone first.")
        self.assertEqual(drone.execute_command("RIGHT"), "Drone is not in the air. Please launch the drone first.")
        self.assertEqual(drone.execute_command("STATUS"), "Drone is not in the air. Please launch the drone first.")
        # Launch the drone
        drone.execute_command("LAUNCH 0,0,NORTH")
        # Now the drone should respond to commands
        self.assertEqual(drone.execute_command("FLY"), None)  # No output expected, just move
        self.assertEqual(drone.execute_command("LEFT"), None)  # Rotate left
        self.assertEqual(drone.execute_command("STATUS"), (0, 1, "WEST"))  # After left, it should face WEST

if __name__ == '__main__':
    # Set verbosity to 2 to show detailed output
    unittest.main(verbosity=2)