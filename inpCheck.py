def get_safe_int(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


age = get_safe_int("Enter your age: ")
print(f"Great, you are {age} years old!")
rollnum = get_safe_int("Enter your roll num: ")
print(f"your roll num is {rollnum}")
  