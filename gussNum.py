import random
num = random.randint(1, 20)
print(num , " is random")

while True:
 guess = int(input("Guess the Integer between 1-20 : "))
 if num == guess:
  print("You are Correct")
  break
 elif (num>guess):
  print("low")
 elif (num<guess):
  print("High")
 else :
  print("Enter a valid integer")
