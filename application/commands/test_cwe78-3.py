import os

def read_file(file_path):
    # Vulnerable: Using user input directly in a command
    os.system(f"cat {file_path}")

# Example usage
user_input = input("Enter the file path to read: ")
read_file(user_input)


