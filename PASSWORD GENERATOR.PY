#password generaotor
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password (default is 12): ") or 12)
    password = generate_password(length)
    print("Generated password:", password)

if __name__ == "__main__":
    main()
