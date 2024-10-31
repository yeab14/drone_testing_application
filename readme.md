# Drone Simulation

This is a simple simulation of a drone flight within a restricted area. The drone can be launched to specific coordinates and can respond to various commands.

## How to Run

1. Clone the repository or download the code.
2. Navigate to the project directory.
3. Run the application using Python: python main.py 
4. Enter commands for the drone as prompted.

## Commands
- `LAUNCH X,Y,DIRECTION` - Launch the drone to the specified coordinates and direction.
- `FLY` - Move the drone forward in the direction it is currently facing.
- `LEFT` - Rotate the drone 90 degrees to the left.
- `RIGHT` - Rotate the drone 90 degrees to the right.
- `STATUS` - Get the current status (position and facing direction) of the drone.

## Project Structure
- `drone.py`: Contains the Drone class with its logic.
- `main.py`: Entry point for user interaction.
- `tests/`: Contains test cases for validating drone functionality.

