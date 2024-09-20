import os

def list_files(directory):
    # Vulnerable: Directly using user input in a system command
    os.system(f"ls {directory}")

# Example usage
user_input = input("Enter the directory to list files: ")
list_files(user_input)
