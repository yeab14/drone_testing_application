# main.py

from commands import process_commands

def main():
    commands = [
        "LAUNCH 0,0,SOUTH",
        "FLY",
        "STATUS",
        "LAUNCH 0,0,NORTH",
        "LEFT",
        "STATUS",
        "LAUNCH 1,2,EAST",
        "FLY",
        "FLY",
        "STATUS",
        "LEFT",
        "FLY",
        "STATUS"
    ]
    
    outputs = process_commands(commands)
    for output in outputs:
        print(output)

if __name__ == "__main__":
    main()
