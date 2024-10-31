from drone import Drone

def main():
    drone = Drone()

    while True:
        command = input("Enter command (or 'exit' to quit, 'save' to save state, 'load' to load state): ").strip()
        if command.lower() == 'exit':
            break
        elif command.lower() == 'save':
            drone.save_state()
            print("Drone state saved.")
            continue
        elif command.lower() == 'load':
            drone.load_state()
            print("Drone state loaded.")
            continue
        
        result = drone.execute_command(command)
        if result is not None:
            print(result)

if __name__ == "__main__":
    main()
