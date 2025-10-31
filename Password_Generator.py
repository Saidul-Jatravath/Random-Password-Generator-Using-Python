from random import sample, shuffle, choice
import string

def password_generator(length, upper_case, lower_case, special_symbols, digits):
    password = []
    all_chars = ""
    
    if upper_case.lower() == "yes":
        all_chars += string.ascii_uppercase
        password.append(choice(string.ascii_uppercase))  # Ensure at least one uppercase letter
    
    if lower_case.lower() == "yes":
        all_chars += string.ascii_lowercase
        password.append(choice(string.ascii_lowercase))  # Ensure at least one lowercase letter
    
    if special_symbols.lower() == "yes":
        all_chars += string.punctuation
        password.append(choice(string.punctuation))  # Ensure at least one special symbol
    
    if digits.lower() == "yes":
        all_chars += string.digits
        password.append(choice(string.digits))  # Ensure at least one digit
    
    if not all_chars:
        print("Please enable at least one character type.")
        return None

    # Fill the rest of the password length with random choices
    password.extend(sample(all_chars, length - len(password)))
    shuffle(password)  # Shuffle to remove predictable patterns
    return "".join(password)

# User inputs
length = int(input("Enter length of your password: "))
upper_case = input("Need uppercase in password (yes/no): ")
lower_case = input("Need lowercase in password (yes/no): ")
special_symbols = input("Need special symbols in password (yes/no): ")
digits = input("Need digits in password (yes/no): ")

# Generate password
password = password_generator(length, upper_case, lower_case, special_symbols, digits)

# Display output
if password:
    print(f"Your generated password is: {password}")
else:
    print("No password generated due to invalid input.")