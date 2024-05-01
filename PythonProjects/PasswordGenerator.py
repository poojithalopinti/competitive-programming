import random
import string

def generate_password(length):
    # Define character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the length is at least 8 characters
    length = max(8, length)

    # Generate the password using random.choice
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    try:
        # Prompt the user for the desired length of the password
        password_length = int(input("Enter the desired length of the password: "))
        
        # Generate the password
        generated_password = generate_password(password_length)
        
        # Display the generated password
        print(f"\nGenerated Password: {generated_password}")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
