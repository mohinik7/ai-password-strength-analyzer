from ml_model import predict_strength

def test_password_strength():
    # Test cases with varying password strengths
    test_passwords = [
        "password123",  # Weak password
        "P@ssw0rd!",    # Medium password
        "Kj#9mP2$vL5nX",  # Strong password
        "12345678",     # Very weak password
        "Qwerty123!",   # Medium password
    ]
    
    print("Testing password strength predictions with new enhanced model:")
    print("-" * 50)
    
    for password in test_passwords:
        strength = predict_strength(password)
        print(f"Password: {password}")
        print(f"Predicted Strength: {strength}")
        print("-" * 50)

if __name__ == "__main__":
    try:
        test_password_strength()
    except Exception as e:
        print(f"Error during testing: {str(e)}") 