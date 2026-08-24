import random
import string

length = int(input("Input length password (minimum 4): "))

def generate_password(length):
    if length < 4:
        raise ValueError("The password length must be at least 4")

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # so that there is at least one character of each type
    password_chars = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols),
    ]

    all_characters = letters + digits + symbols
    for _ in range(length - 3):
        password_chars.append(random.choice(all_characters))

    random.shuffle(password_chars)  # shake for more random
    return "".join(password_chars)

print("your password:", generate_password(length))