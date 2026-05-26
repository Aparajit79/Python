import string
import random


def passwordGenerator(length):
    password = ""
    pool = string.ascii_letters + string.digits + string.punctuation

    for i in range(length):
        password += random.choice(pool)

    return password

length = int(input("Enter the length of password to generate : "))
print(passwordGenerator(length))

