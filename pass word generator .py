import string
import random

def generate_password(length):
    """Generate a strong password of given length."""
    if length < 8:
        print("Your password length should be at least 8 characters.")
        return None

    characters = []
    characters.extend(random.sample(string.ascii_lowercase, length // 6))
    characters.extend(random.sample(string.ascii_uppercase, length // 6))
    characters.extend(random.sample(string.digits, length // 6))
    characters.extend(random.sample(string.punctuation, length // 6))
    characters.extend(random.sample(string.ascii_letters + string.digits + string.punctuation, length - 3 * (length // 6)))

    random.shuffle(characters)

    return ''.join(characters)

def get_valid_length():
    """Get a valid length for the password from the user."""
    while True:
        try:
            length = int(input("How many characters do you want in your password? "))
            if length < 8:
                print("Your password length should be at least 8 characters.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        length = get_valid_length()
        password = generate_password(length)
        if password:
            print("Strong Password:", password)

        another_password = input("Do you want to generate another password? (yes/no): ")
        if another_password.lower() != "yes":
            break

if   __name__ == "_main_":
    main()