# test_commands.py

from commands import process_commands

def test_drone_commands():
    commands = [
        "LAUNCH 0,0,NORTH",
        "FLY",          # Expect the drone to move to (0,1)
        "STATUS",      # Expect 0,1,NORTH
        "RIGHT",       # Expect facing EAST
        "FLY",         # Expect the drone to move to (1,1)
        "STATUS",      # Expect 1,1,EAST
        "LEFT",        # Expect facing NORTH
        "FLY",         # Expect the drone to move to (1,2)
        "FLY",         # Expect the drone to move to (1,3)
        "STATUS",      # Expect 1,3,NORTH
        "LAUNCH 5,5,WEST",  # Invalid launch
        "STATUS"       # Expect 1,3,NORTH (no change)
    ]

    outputs = process_commands(commands)
    for output in outputs:
        print(output)

if __name__ == "__main__":
    test_drone_commands()

