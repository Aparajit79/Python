while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Please Enter a valid integer")

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print("Number not divisible by 3 and 5")
