import os
import shlex
import subprocess
def validate_command(cmd):
    splitted_cmd = cmd.split()
    if not splitted_cmd or splitted_cmd[0] not in SAFE_COMMANDS:
        raise ValueError('Command not allowed')

SAFE_COMMANDS = {'ls', 'cd'}

def read_file(file_path):
    # Vulnerable: Using user input directly in a command
    validate_command(file_path)
    cmd_list = shlex.split(f"cat {file_path}")
    subprocess.run(cmd_list, check=True, shell=False)

# Example usage
user_input = input("Enter the file path to read: ")
read_file(user_input)
