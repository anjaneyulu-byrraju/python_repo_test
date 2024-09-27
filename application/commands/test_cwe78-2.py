import os
from flask import Flask, request
import shlex
import subprocess
def validate_command(cmd):
    splitted_cmd = cmd.split()
    if not splitted_cmd or splitted_cmd[0] not in SAFE_COMMANDS:
        raise ValueError('Command not allowed')

SAFE_COMMANDS = {'ls', 'cd'}

app = Flask(__name__)

@app.route('/run')
def run_command():
    # Vulnerable: Directly using URL parameter in a system command
    command = request.args.get('command')
    validate_command(command)
    cmd_list = shlex.split(command)
    subprocess.run(cmd_list, check=True, shell=False)
    return "Command executed"

if __name__ == "__main__":
    app.run()
