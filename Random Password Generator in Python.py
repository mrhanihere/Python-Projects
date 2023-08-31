import random
import string

length = int(input("Enter the password length: "))

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(length))
print("Random Password:", password)
