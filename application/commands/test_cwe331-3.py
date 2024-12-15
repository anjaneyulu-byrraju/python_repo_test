import random
import string

def generate_reset_token():
    # Vulnerable: using random.choice() for token generation
    rand = random.SystemRandom()
    token = ''.join(rand.choice(string.ascii_letters + string.digits) for _ in range(10))
    return token

# Example usage
reset_token = generate_reset_token()
print(f"Generated reset token: {reset_token}")
