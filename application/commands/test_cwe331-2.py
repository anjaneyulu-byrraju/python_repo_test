import random

def generate_iv():
    # Vulnerable: using random.random() for IV generation
    iv = int(random.random() * (2**64))  # Generates a 64-bit IV
    return iv

# Example usage
iv = generate_iv()
print(f"Generated IV: {iv}")
