import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))

    return password


if __name__ == "__main__":
    length = int(input("Enter length password: "))
    password = generate_password(length)
    print(f"Passwod: {password}")
