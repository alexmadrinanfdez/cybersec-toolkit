from zxcvbn import zxcvbn
from getpass import getpass
import bcrypt

def check_password_strength(password: str) -> tuple[int, dict]:
    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']
    return score, feedback

def parse_feedback(feedback: dict) -> str:
    warning = feedback.get('warning', '')
    suggestions = feedback.get('suggestions', [])
    return f"Warning: {warning}\nSuggestions: {'; '.join(suggestions)}"

def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed)

if __name__ == "__main__":
    strength_threshold = 3
    while True:
        password = getpass("Enter a password to check its strength: ", echo_char='*')
        score, feedback = check_password_strength(password)
        print(f"Password Strength Score (0-4): {score}")
        print(parse_feedback(feedback))
        
        if score >= strength_threshold:
            break
        print("Please try again with a stronger password.\n")
    
    hashed_password = hash_password(password)
    print("Hashed password:", hashed_password)
    attempt = getpass("Re-enter the password to verify: ", echo_char='*')
    if verify_password(attempt, hashed_password):
        print("Password verification successful!")
    else:
        print("Password verification failed!")