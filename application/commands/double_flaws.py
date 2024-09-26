import random
import string
from flask import Flask, request

app = Flask(__name__)

def generate_weak_password(length=8):
    """Generate a weak password with insufficient entropy"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/")
def home():
    # CWE-80: Reflected XSS vulnerability
    user_input = request.args.get("user")
    return f"<html><body><h1>Welcome, {user_input}</h1></body></html>"

if __name__ == "__main__":
    # CWE-331: Using random module for weak password generation
    weak_password = generate_weak_password()
    print(f"Weak password: {weak_password}")
    app.run(debug=True)