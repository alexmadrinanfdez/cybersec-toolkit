from zxcvbn import zxcvbn

def check_password_strength(password: str) -> tuple[int, dict]:
    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']
    return score, feedback

def parse_feedback(feedback: dict) -> str:
    warning = feedback.get('warning', '')
    suggestions = feedback.get('suggestions', [])
    return f"Warning: {warning}\nSuggestions: {'; '.join(suggestions)}"

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    score, feedback = check_password_strength(password)
    print(f"Password Strength Score (0-4): {score}")
    print(parse_feedback(feedback))