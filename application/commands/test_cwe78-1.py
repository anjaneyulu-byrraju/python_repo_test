import os
import shlex
import subprocess
def validate_command(cmd):
    splitted_cmd = cmd.split()
    if not splitted_cmd or splitted_cmd[0] not in SAFE_COMMANDS:
        raise ValueError('Command not allowed')

SAFE_COMMANDS = {'ls', 'cd'}

def list_files(directory):
    # Vulnerable: Directly using user input in a system command
    validate_command(directory)
    cmd_list = shlex.split(f"ls {directory}")
    subprocess.run(cmd_list, check=True, shell=False)

# Example usage
user_input = input("Enter the directory to list files: ")
list_files(user_input)
