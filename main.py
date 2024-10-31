from drone import Drone

def main():
    drone = Drone()
    
    while True:
        command = input("Enter command (or 'exit' to quit): ").strip()
        if command.lower() == 'exit':
            break
        
        result = drone.execute_command(command)
        if result is not None:
            print(result)

if __name__ == "__main__":
    main()
