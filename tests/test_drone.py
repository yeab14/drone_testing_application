import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
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

if __name__ == '__main__':
    unittest.main()