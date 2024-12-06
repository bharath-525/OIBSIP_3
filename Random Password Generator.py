import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    # Define the character set based on user preferences
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    # Ensure there's at least one character type selected
    if not characters:
        raise ValueError("At least one character type must be selected")

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    # Get user inputs
    try:
        length = int(input("Enter password length: "))
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Generate the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
