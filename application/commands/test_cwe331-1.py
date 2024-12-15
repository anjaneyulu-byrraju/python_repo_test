import random
import secrets

def generate_key():
    # Vulnerable: using random.randint() for key generation
    key = secrets.randint(0, 2**32 - 1)  # Generates a 32-bit key
    return key

# Example usage
key = generate_key()
print(f"Generated key: {key}")
