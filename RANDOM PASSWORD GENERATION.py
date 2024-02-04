import random
import string

def generate_password(length):
    return ''.join(random.choices(string.ascii_letters+string.digits+string.punctuation,k=length))

def main():
    length=int(input("Enter the length of the password: "))
    print("Generated Password:",generate_password(length))

if __name__ == "__main__":
    main()
