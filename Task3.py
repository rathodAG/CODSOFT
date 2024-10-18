import random  # Import the random module to generate random numbers
import string  # Import the string module to access string constants

def generate_password(length):
    
    # Define character sets
    lowercase = string.ascii_lowercase  # String of lowercase letters
    uppercase = string.ascii_uppercase  # String of uppercase letters
    digits = string.digits  # String of digits (0-9)
    special_characters = string.punctuation  # String of special characters

    # Combine character sets into one string
    all_characters = lowercase + uppercase + digits + special_characters

    # Generate a random password by selecting characters from the combined set
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password  # Return the generated password

def evaluate_password_strength(password):
    # Determine strength based on length
    if len(password) >= 10:
        return "Strong"  # Return "Strong" if the password is 12 characters or longer
    elif len(password) >= 7:
        return "Moderate"  # Return "Moderate" if the password is at least 8 characters
    else:
        return "Weak"  # Return "Weak" for passwords shorter than 8 characters

def main():
    while True:
        try:
            # Prompt user for the desired password length
            length = int(input("Enter the desired length of the password (minimum 7): "))
            if length < 7:
                print("Please enter a length of at least 7 characters.")  # Warn user if length is too short
                continue  # Continue to the next iteration of the loop
            break  # Exit the loop if valid length is provided
        except ValueError:
            print("Invalid input. Please enter a number.")  # Handle non-integer inputs

    # Generate the password
    password = generate_password(length)

    # Evaluate the strength of the password
    strength = evaluate_password_strength(password)

    # Display the password and its strength
    print(f"Generated Password: {password}")  # Print the generated password
    print(f"Password Strength: {strength}")  # Print the strength of the password

# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    main()  # Call the main function to execute the program