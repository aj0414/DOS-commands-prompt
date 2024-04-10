import os
import subprocess
import tkinter as tk

def display_commands():
    command_list = [
        "Display the current directory path (cd)",
        "View directory contents (dir)",
        "Create a new directory (md <dir name>)",
        "Change directory (cd <dir path>)",
        "cd..",
        "Display file contents (type <file name>)",
        "Copy files (copy <source> <destination>)",
        "Rename a file or directory (ren <old name> <new name>)",
        "Remove a directory (rmdir <dir name>)",
        "Delete a file (del <file name>)",
        "Date",
        "Time",
        "Clear the screen (cls)",
        "Exit"
    ]

    for index, command in enumerate(command_list, start=1):
        tk.Button(root, text=command, command=lambda cmd=command: execute_command(cmd)).grid(row=index, column=0, padx=10, pady=5)

def execute_command(command):
    choice = command.split()[0]
    if choice == "Display":
        print("Current directory path:", os.getcwd())
    elif choice == "View":
        subprocess.run(["dir"], shell=True)
    elif choice == "Create":
        new_dir_name = input("Enter the directory name: ")
        os.mkdir(new_dir_name)
    elif choice == "Change":
        new_dir_path = input("Enter the directory path: ")
        os.chdir(new_dir_path)
        print("Changed directory to:", new_dir_path)
    elif choice == "cd..":
        os.chdir("..")
        print("Changed directory to parent directory.")
    elif choice == "Display":
        file_to_display = input("Enter the file name to display contents: ")
        with open(file_to_display, 'r') as file:
            print(file.read())
    elif choice == "Copy":
        copy_params = input("Enter source followed by destination separated by space: ")
        subprocess.run(["copy"] + copy_params.split(), shell=True)
    elif choice == "Rename":
        rename_params = input("Enter the old name followed by the new name separated by space: ")
        subprocess.run(["ren"] + rename_params.split(), shell=True)
    elif choice == "Remove":
        dir_to_remove = input("Enter the directory name to remove: ")
        subprocess.run(["rmdir", "/S", "/Q", dir_to_remove], shell=True)
    elif choice == "Delete":
        file_name_to_delete = input("Enter the file name to delete: ")
        os.remove(file_name_to_delete)
    elif choice == "Date":
        subprocess.run(["date", "/t"], shell=True)
    elif choice == "Time":
        subprocess.run(["time", "/t"], shell=True)
    elif choice == "Clear":
        clear_screen()
    elif choice == "Exit":
        print("Exiting...")
        exit()

def clear_screen():
    # Clear the screen
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("DOS Commands")
    display_commands()
    root.mainloop()
