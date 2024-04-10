import os

def run_command(command):
    if command.startswith("cd "):
        try:
            # Extract the directory to change to
            directory = command.split(maxsplit=1)[1]
            os.chdir(directory)
            print(f"Changed directory to {os.getcwd()}")
        except Exception as e:
            print(f"Error changing directory: {e}")
    else:
        os.system(command)

def main():
    commands = {
        '1': ('View directory contents (dir)', 'dir'),
        '2': ('Display the current directory path (cd)', 'cd .'),
        '3': ('Clear the screen (cls)', 'cls'),
        '4': ('Create a new directory (md <dir name>)', 'md'),
        '5': ('Delete a file (del <file name>)', 'del'),
        '6': ('Remove a directory (rmdir <dir name>)', 'rmdir /S /Q'),
        '7': ('Change directory (cd <dir path>)', 'cd '),
        '8': ('Rename a file or directory (ren <old name> <new name>)', 'ren'),
        '9': ('Display file contents (type <file name>)', 'type'),
        '10': ('Copy files (copy <source> <destination>)', 'copy'),
        '11': ('Exit', 'exit')
    }

    while True:
        print("\nAvailable DOS Commands:")
        for key in sorted(commands.keys(), key=int):
            print(f"{key}. {commands[key][0]}")
        
        choice = input("\nEnter the number of the command you want to execute (or '11' to exit): ")
        
        if choice == '11':
            print("Exiting...")
            break

        if choice in commands:
            if commands[choice][1] in ['md', 'del', 'rmdir /S /Q', 'cd ', 'ren', 'type', 'copy']:
                additional_input = input(f"Enter the necessary parameter(s) for the command '{commands[choice][0]}': ")
                full_command = f"{commands[choice][1]} {additional_input}"
            else:
                full_command = commands[choice][1]

            print(f"Executing: {full_command}")
            run_command(full_command)
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
