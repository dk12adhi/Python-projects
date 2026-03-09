#PASSWORD VALIDATOR


import string

def check_password(p):
    is_long = len(p) >= 8
    lower = any(char.islower() for char in p)
    upper = any(char.isupper() for char in p)
    digit = any(char.isdigit() for char in p)
    special = any(char in string.punctuation for char in p)
    
    if all([is_long, upper, lower, digit, special]):
        return True
    else:
        return False

while True:
    password = input("Enter a password: ")
    
    if check_password(password):
        print("Your password is valid")
        break
    else:
        print("Invalid password, try again")
        
