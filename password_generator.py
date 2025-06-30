import re # regular expression library it helps us to check the password
import secrets # library to generate random password
import string


def generate_password(length, nums, special_chars, uppercase, lowercase): # Defines a function to create a password with given conditions
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_characters = letters + digits + symbols  # Combine all character types

    # Keeps generating new password until all rules are met                                                                                                                                      
    while True:
        password = ''
        for _ in range(length):
            password += secrets.choice(all_characters) # Randomly pick characters
        
        constraints = [
            (nums, r'\d'),
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),
            (special_chars, fr'[{symbols}]')
        ]

        if all(constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraints):
            break # If all conditions are satisfied, stop loop

    return password


pattern = re.compile('l+')
quote = 'Not all those who wander are lost.'
print(pattern.search(quote))


if __name__ == '__main__':  # Runs the following only if the script is run directly
    
    # Calls the password generator with rules and prints the result
    new_password = generate_password(length=8, nums=1, special_chars=1, uppercase=1, lowercase=1)
    print('Generated password:', new_password)