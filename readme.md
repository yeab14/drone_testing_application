# Drone Simulation

This project simulates a drone that can be controlled with simple commands for launching, flying, and changing direction. It tracks the drone's state and logs commands for reference.

## Features

- **Control Commands**:
  - `LAUNCH x,y,DIRECTION`: Launch the drone at coordinates (x,y) facing a specified direction (NORTH, EAST, SOUTH, WEST).
  - `FLY`: Move the drone forward in its current direction.
  - `LEFT` / `RIGHT`: Rotate the drone 90 degrees.
  - `STATUS`: Report current position and direction.

- **Logging**: Command history is saved in a `history.txt` file.
- **State Management**: Save and load the drone's state in JSON format.

## Getting Started

1. **Installation**:
   - Clone the repository and install Python (3.x recommended).
   - (Optional) Set up a virtual environment.

2. **Run the Simulation**:
   ```bash
   python test_drone.py


## Testing 

This project includes unit tests to validate functionality. You can run all tests using:  
```bash
python -m unittest test_drone.py 
```

## Test Cases

The tests utilize the `unittest` framework and cover the following scenarios:

## 1. Test Fly (`test_fly`)

**Description**: Verifies the forward movement of the drone in its current direction.  
**Assertions**: Confirms the new position after flying and checks boundaries to prevent out-of-bounds movements.
**Command**:
```bash
python -m unittest test_drone.TestDrone.test_fly
```

## 2. Test Fly Out of Bounds (`test_fly_out_of_bounds`)

**Description**: Verifies the behavior when the drone tries to fly out of bounds.
**Assertions**: Ensures the drone does not exceed the defined testing area.
**Command**:
```bash 
python -m unittest test_drone.TestDrone.test_fly_out_of_bounds
```

## 3. Test Launch Valid (`test_launch_valid`)

**Description**: Tests the valid drone launch functionality.
**Assertions**: Ensures the drone correctly updates its position and direction when launched.
**Command**:
```bash 
python -m unittest test_drone.TestDrone.test_launch_valid
```

## 4. Test Rotate Left (`test_rotate_left`)

**Descriptions**: Verifies that the drone can rotate left.
**Assertions**: Ensures the direction updates correctly after each left turn.
**Command**: 
``` bash
python -m unittest test_drone.TestDrone.test_rotate_left
```

## 5.  Test Rotate Right (`test_rotate_right`)

**Description**: Verifies that the drone can rotate right.
**Assertions**:  Ensures the direction updates correctly after each right turn.
**Command**: 
``` bash 
python -m unittest test_drone.TestDrone.test_rotate_right
```

## 6. Test Save and Load State (`test_save_load_state`)

**Descriptions**: Tests saving and loading the drone's state from a JSON file.
**Assertions**: Compares the drone’s state before and after loading from the file.
**Command**: 
``` bash 
python -m unittest test_drone.TestDrone.test_save_load_state
```

## 7. Test Status When Not in Air (`test_status_when_not_in_air`)

**Descriptions**: Validates that the status command reports the correct position and direction when the drone is not in the air.
**Assertions**: Compares reported status to expected values when the drone is grounded.
**Command**:
``` bash 
python -m unittest test_drone.TestDrone.test_status_when_not_in_air
```

## 8. Test Status (`test_status`)

**Description**: Verifies that the status command correctly reports the drone's position and direction after it has been launched.
**Assertion**:Ensures that the status of the drone matches the expected coordinates and direction after launching it.
**Command**: 
``` bash 
 python -m unittest test_drone.TestDrone.test_status
```

## 9. Test Ignore Invalid Commands (`test_ignore_invalid_commands`) 

**Description**: Validates that the drone ignores commands before launch and reports an appropriate message.
**Assertion**: Ensures that all commands (FLY, LEFT, RIGHT, STATUS) return a message indicating the drone must first be launched.
**Command**: 
``` bash 
python -m unittest test_drone.TestDrone.test_ignore_invalid_commands
```


## Conclusion

This drone simulation project is designed to accurately model the behavior of a drone based on simple control commands. The tests implemented ensure the reliability and correctness of the drone’s functionality. By running the tests, we have verified the following:

- **Movement and Direction**: The drone moves forward in the specified direction when the `FLY` command is issued. The direction is updated correctly when the `LEFT` or `RIGHT` commands are used, ensuring that the drone follows the expected path.
  
- **Boundary Safety**: The `FLY` command respects the predefined boundary limits. If the drone attempts to move beyond the designated area, it either stops or prevents further movement, ensuring no out-of-bounds errors occur.

- **Launching**: The `LAUNCH` command correctly initializes the drone at the specified coordinates and direction, ensuring that the drone starts from the correct position.

- **State Management**: The ability to save and load the drone’s state ensures that its progress can be tracked, and no data is lost between sessions.

- **Command Logging**: All issued commands are logged to a history file (`history.txt`), providing a detailed record of the drone’s activity.

These tests help ensure that the core features of the drone simulation—movement, boundary management, launching, and state persistence—function as expected under various scenarios. With these validations in place, the simulation is ready for further development or integration into larger systems.







