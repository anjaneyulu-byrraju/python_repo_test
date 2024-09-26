import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/run')
def run_command():
    # Vulnerable: Directly using URL parameter in a system command
    command = request.args.get('command')
    os.system(command)
    return "Command executed"

if __name__ == "__main__":
    app.run()

    