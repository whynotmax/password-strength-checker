import re
import random
import string

def check_password_strength(password):
    strength = "Weak"
    suggestions = []

    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long.")
    if not re.search("[a-z]", password):
        suggestions.append("Password should include lowercase letters.")
    if not re.search("[A-Z]", password):
        suggestions.append("Password should include uppercase letters.")
    if not re.search("[0-9]", password):
        suggestions.append("Password should include numbers.")
    if not re.search("[@#$%^&+=]", password):
        suggestions.append("Password should include symbols (e.g., @, #, $, etc.).")
    if re.search(r"(.)\1\1", password):
        suggestions.append("Password should not have sequences of repeated characters.")
    if re.search(r"(12345|abcdef|password|qwerty)", password, re.IGNORECASE):
        suggestions.append("Password should not contain common patterns or words.")

    if len(password) >= 8 and re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password) and re.search("[@#$%^&+=]", password):
        strength = "Strong"
    elif len(password) >= 6 and (re.search("[a-z]", password) or re.search("[A-Z]", password)) and re.search("[0-9]", password):
        strength = "Moderate"

    return strength, suggestions

def time_to_crack(password_length, char_set_size, guesses_per_second):
    total_combinations = char_set_size ** password_length

    time_in_seconds = total_combinations / guesses_per_second

    if time_in_seconds < 1:
        return "Instantly"

    time_units = [("Years", 60 * 60 * 24 * 365),
                  ("Months", 60 * 60 * 24 * 30),
                  ("Days", 60 * 60 * 24),
                  ("Hours", 60 * 60),
                  ("Minutes", 60),
                  ("Seconds", 1)]
    
    for unit, seconds_in_unit in time_units:
        if time_in_seconds >= seconds_in_unit:
            time_in_unit = time_in_seconds / seconds_in_unit
            return f"{time_in_unit:.2f} {unit}"
    
    return "Instantly"

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    character_set = ""
    if use_upper:
        character_set += string.ascii_uppercase
    if use_lower:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_symbols:
        character_set += "@#$%^&+="

    if not character_set:
        raise ValueError("At least one character type must be selected")

    return ''.join(random.choice(character_set) for _ in range(length))

def main():
    while True:
        print("\nPassword Strength Checker")
        print("1. Check password strength")
        print("2. Generate a strong password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            password = input("Enter a password to check: ")
            strength, suggestions = check_password_strength(password)
            print(f"Password Strength: {strength}")
            if suggestions:
                print("Suggestions to improve your password:")
                for suggestion in suggestions:
                    print(f"- {suggestion}")
            timeToCrack = time_to_crack(len(password), 94, 1000000000)
            print(f"Time to crack (approximate): {timeToCrack}")
        elif choice == '2':
            length = int(input("Enter the desired length of the password: "))
            use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
            use_digits = input("Include numbers? (y/n): ").lower() == 'y'
            use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
            password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
            print(f"Generated Password: {password}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()